# coding: utf-8
__author__ = "wengwenyu"
import re
from datetime import datetime, timedelta
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import VerifyCode
from django.contrib.auth import get_user_model
from LeShop import settings

User = get_user_model()


# 发送验证码的时候，他传手机号
class SmsSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11, label="手机号", help_text="请输入手机号")

    # validate_ + 字段名字
    def validate_mobile(self, mobile):
        # 1. 验证是否注册 13683084940
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError("用户已经注册")

        # 2. 正则表达式
        if not re.match(settings.REGEX_MOBILE, mobile):
            raise serializers.ValidationError("手机号不正确")

        # 3 判断频率
        one_minutes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_minutes_ago, mobile=mobile).count():
            raise serializers.ValidationError("60s内只能发送一次短信")

        return mobile


# 注册
class UserRegSerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_length=4, min_length=4, error_messages={
        "max_length": "验证码格式不对",
        "min_length": "验证码格式不对"
    }, label="验证码", write_only=True)

    username = serializers.CharField(
        label="用户名",
        validators=[UniqueValidator(queryset=User.objects.all(), message="用户已存在")]
    )

    # 使用 <input type="password"> 作为输入。
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True
    )

    def create(self, validated_data):
        user = super().create(validated_data=validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    def validate_code(self, code):
        # 1. 验证码正确性 2. 时效
        # initial_data 用户从客户端post 过来的数据
        # 16619983290这个手机号下的所有验证码  [1234,5678,9876]
        verify_records = VerifyCode.objects.filter(mobile=self.initial_data["username"]).order_by("-add_time")

        if verify_records:
            # 用户发送过验证码
            # 判断 时间
            last_recode = verify_records[0]
            five_minutes_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
            if five_minutes_ago > last_recode.add_time:
                raise serializers.ValidationError("验证码过期")

            if code != last_recode.code:
                raise serializers.ValidationError("验证码错误")

        else:
            # 用户根本没有发送过验证码
            raise serializers.ValidationError("请输入正确的验证码!")

    def validate(self, attrs):
        attrs['mobile'] = attrs['username']
        del attrs['code']
        return attrs

    class Meta:
        model = User
        fields = ("username", "mobile", "code", 'password')

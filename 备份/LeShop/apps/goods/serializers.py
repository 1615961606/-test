# coding: utf-8
__author__ = "wengwenyu"

# 1. DRF的序列化模块
from rest_framework import serializers
# 模型类
from .models import Goods, GoodsCategory, Banner


class GoodsSerializer(serializers.ModelSerializer):
    """商品"""

    class Meta:
        model = Goods
        fields = "__all__"


class CategorySerializer3(serializers.ModelSerializer):
    """三级类目"""

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    """二级类目"""
    sub_cat = CategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):  # 1
    """一级类目"""
    sub_cat = CategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


# 序列化的嵌套


# 首页轮播图的序列化
class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"

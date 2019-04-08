# coding: utf-8
__author__ = "wengwenyu"
import requests
import json


class YuanPian(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_sms(self, code, mobile):
        # 让云片网发送短信验证码  我们需要传哪些参数
        params = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": "【大家庭】您的验证码是{}。如非本人操作，请忽略本短信".format(code)
        }
        # 发起一个网络请求  得到相应
        response = requests.post(self.single_send_url, data=params)
        ret = json.loads(response.text)
        return ret


if __name__ == '__main__':
    # 测试
    yun_pian = YuanPian("c60770e37f172c235b9b3c0380807108")
    r = yun_pian.send_sms('lxd', '17640614938')
    print(r)

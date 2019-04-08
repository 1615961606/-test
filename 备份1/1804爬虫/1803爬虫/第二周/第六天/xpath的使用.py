# /根节点
# //任意位置获取节点
# .当前节点
# ..当前节点的父节点
# @属性名 取属性
# 【@class=''】获取指定属性的节点
# text()获取节点文本

# /book/img[1]:获取book下的第一个img节点
# /book/img[last()]:获取book下的最后一个img节点
import requests
import re
import lxml

url = ''
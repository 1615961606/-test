from urllib import request,parse,error
import ssl

爬虫的流程：
1.寻找目标url
2.分析url,构建请求Request对象
  req = request.Request()
3.根据构建的Request对象发起请求
　response = request.urlopen(req)



注意：
１．（get请求）如果url中带有中文，我们需要使用parse.urlencode(),
将我们的中文参数转换为url格式的编码
２．（post）如果表单数据中出现中文，使用parse.urlencode()将参数
转为url格式的编码，然后使用encode()编码，得到二进制数据
３．爬虫在访问url的时候，要模拟浏览器操作，我们必须设置User-Agent(放在请求头里)


如何或取响应内容：
１．响应的状态码：response.status
2. 响应体：response.read() -> 得到的是一个二进制数据
　　　　　　response.read().decode('编码类型')　->解码得到的是一个字符串
３．响应头：response.getheaders()
4.　原因：response.reason
5. 获取当前请求的url:response.url


# parse模块：对url解析，拆分，合并，编码，解码

parse.urlparse()
parse.urlunparse()

parse.quote()
parse.unquote()

parse.urlencode() key=vaule&key=value&....
parse.parse_qs()

parse.urljoin() 

# 容错：
#error.URLError:
1.没有网络
２．服务器连接失败
３．找不到对应的服务器

URLError只有一个reason属性：

try:
    req = request.Request()
    response = request.urlopen(req)
except error.URLError as err:
    print(err.reason)

#error.HTTPError
1.页面未找到（４０４）
２．服务器错误（500）

具有三个属性:code,headers,reason

try:
    req = request.Request()
    response = request.urlopen(req)
except error.HTTPError as err:
    print(err.code)
    print(err.headers)
    print(err.reason)

最优写法：先判断子类错误，然后在判断父类错误

try:
    req = request.Request()
    response = request.urlopen(req)
except error.HTTPError as err:
    print(err.code)
    print(err.headers)
    print(err.reason)
except error.URLError as err:
    print(err.reason)

#有时候https协议的证书并不是经过CA证书机构办法，我们需要忽略证书认证
context = ssl._create_unverified_context()
req = request.Request()
request.urlopen(req,context=context)

#如何提取数据？？
正则
\d:
\D:
\w:
\W:
\s:空白字符
\S:
^
$
.

+
*
?
{n}
{n,m}

+?
*?
??

()
|

原始字符：
r''

import re
方法：
re.compile(),可以将正则表达式，构建为一个pattern对象
re.match(),
re.search(),
re.findall(),
re.finditer(),
re.sub(),
re.split(),

#json.loads():将json字符串转换为python数据类型
json.loads()

#如何处理得到的提取的数据结果
１．本地文件存储
２．csv文件操作
３．持久化（mysql）






















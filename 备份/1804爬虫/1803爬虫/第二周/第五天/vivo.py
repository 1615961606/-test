import requests
url = 'https://pic.ibaotu.com/00/75/21/04N888piC7nd.mp4'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36'

}
response = requests.get(url,headers=headers)
with open('k.mp4','wb+') as f:
    f.write(response.content)
from multiprocessing import Pool
import requests
def down_load(page,name):
    print(page,name)
    #http://blog.jobbole.com/all-posts/page/2/
    full_url = 'http://blog.jobbole.com/all-posts/page/%s/'%(page)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    response = requests.get(full_url,headers=headers)
    if response.status_code == 200:
        print(response.text)

if __name__ == '__main__':
    #创建一个线程池
    process_poll = Pool(4)

    for page in range(0,100):
        #网进程池里添加进程
        process_poll.apply_async(down_load,(page,'进程池'))
    #关闭进程池，后面不能再添加任务了
    process_poll.close()

    #子进程执行完毕，执行完毕后，再回来执行主进程代码
    process_poll.join()
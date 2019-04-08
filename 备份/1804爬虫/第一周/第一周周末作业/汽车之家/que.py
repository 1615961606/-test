from queue import Queue
from lxml import etree







if __name__ =='__main__':
    page_que = Queue(100)
    img_que = Queue(500)
    for page_num in range(1,101):
        page_que.put("https://www.doutula.com/article/list/?page={}").format(page_num)

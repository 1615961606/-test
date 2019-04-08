# import threading
# import queue



# def write_data(queue):
#     for i in range(0,100):
#         print(threading.current_thread().name+'正在写入'+str(i))
#         queue.put(i)

# def read_data(queue):
#     while queue.empty() is not True:
#         print(threading.current_thread().name+'正在读取'+str(queue.get()))


# if __name__ == '__main__':
#     queue = queue.Queue()

#     w_td = threading.Thread(target=write_data,name='德玛西亚',args=(queue,))
#     w_td.start()

#     w_td.join()

#     r_td = threading.Thread(target=read_data,name='鲁班一号',args=(queue,))
#     r_td.start()

#     r_td.join()

#     print(threading.current_thread().name+'主线程执行完毕')


# from concurrent.futures import ThreadPoolExecutor
# import threading

# def download_data_by_page(page,name):
#     print(page,name)
#     #根据page构建url，发起请求

#     return 'download_done'

# def done(future):
#     print(future.result())

# if __name__ == '__main__':
    
#     print('主线程开始执行'+threading.current_thread().name)
#     #创建一个线程池
#     pool = ThreadPoolExecutor(20)

#     for page in range(1,50):
#         handler = pool.submit(download_data_by_page,page,'clss1804')
#         handler.add_done_callback(done)

#     pool.shutdown() #-> 执行了线程的join()方法

#     print('主线程执行完毕'+threading.current_thread().name)







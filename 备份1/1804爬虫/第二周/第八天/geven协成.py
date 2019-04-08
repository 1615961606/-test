import gevent
import time
def do(num):
    for i in range(0,num):
        time.sleep(1)
        print(gevent.getcurrent(),1)

gev1 = gevent.spawn(do,10)
gev2 = gevent.spawn(do,10)
gev3 = gevent.spawn(do,10)
gev4 = gevent.spawn(do,10)

gev1.join()
gev2.join()
gev3.join()
gev4.join()


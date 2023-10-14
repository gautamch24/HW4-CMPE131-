import time
def timestamp(func):
    def innerFunc():
       print(time.ctime())
       func()
    return innerFunc()

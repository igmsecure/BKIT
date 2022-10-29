from time import time
from contextlib import contextmanager

class cm_timer_1:
    def __init__(self):
        self.__start = time()
    def __enter__(self):
        return self
    def __exit__(self, type, value, traceback):
        print('time: ', round(time() - self.__start, 2))

@contextmanager
def cm_timer_2():
    start = time()
    yield
    time_end = time()
    print('time: ', round(time() - start, 2))
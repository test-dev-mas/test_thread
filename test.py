import threading
import time

class A(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        print("hello world")
        time.sleep(2)

if __name__ == '__main__':
    a = A()
    a.start()
    print(a.is_alive())         # immediately after thread starts, it should be alive
    time.sleep(2)
    print(a.is_alive())         # it should be done by now
import threading
import time


def thread_job():
    print('T1 start')
    for i in range(10):
        time.sleep(1)


if __name__ == '__main__':
    thread1 = threading.Thread(target=thread_job(), name='T1')
    thread1.start()
    print(threading.current_thread())

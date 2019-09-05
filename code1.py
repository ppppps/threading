import multiprocessing as mp
import threading as td


def job(q):
    res = 0
    for i in range(1000):
        res += i + pow(i, 2) + pow(i, 3)
    q.put(res)


# t1 = td.Thread(target=job, args=(1,2))
if __name__ == '__main__':
    q = mp.Queue()

    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))  # 这个逗号不能少！！

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print(res1 + res2)

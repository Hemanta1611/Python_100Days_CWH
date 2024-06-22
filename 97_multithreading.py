"""
import threading
import time


# indicates some task being done
def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)


# time1 = time.perf_counter()
# # Normal code
# func(4)
# func(2)
# func(1)
# func(7)
# time2 = time.perf_counter()
# print("time for executing normally: ", time2-time1)


# same code using threads
t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[2])
t3 = threading.Thread(target=func, args=[1])
t4 = threading.Thread(target=func, args=[7])

time3 = time.perf_counter()
t1.start()
t2.start()
t3.start()
t4.start()

# Whenever this method is called for any Thread object, it blocks the calling thread till the time the thread whose join() method is called terminates
t1.join()
t2.join()
t3.join()
t4.join()
time4 = time.perf_counter()
print("time for executing using thread: ", time4-time3)


print("hii")

"""





import threading
import time
from concurrent.futures import ThreadPoolExecutor


def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)


def poolingDemo():
    with ThreadPoolExecutor() as executor:
        # future1 = executor.submit(func, 3)
        # print(future1.result())
        # future2 = executor.submit(func, 2)
        # print(future2.result())
        # future3 = executor.submit(func, 4)
        # print(future3.result())
        # future1 = executor.submit(func, 3)
        # future2 = executor.submit(func, 2)
        # future3 = executor.submit(func, 4)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())

        l = [3, 2, 4]
        results = executor.map(func, l)
        for result in results:
            print(result)


poolingDemo()






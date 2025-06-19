# Processes that run in parallel, 
# when to use: cpu-bound tasks that are heavy on cpu usage(ex: image processing, mathematical computation), parallel exectution
# when not to use: io-bound tasks that are heavy on disk usage(ex: file reading, file writing)

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Cube: {i*i*i}")

if __name__ == "__main__":
    # create the 2 processes
    t = time.time()

    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finish_time = time.time() - t
    print(f"finish time: {finish_time}")


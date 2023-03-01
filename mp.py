from multiprocessing import Process
import os
import pandas as pd
import numpy as np
import time


def worker(wData):
    count = 0
    print("Worker {}".format(os.getpid()))
    print("Data length: {}".format(len(wData)))
    for line in wData:
        print("Worker {}, Line {}: {}".format(os.getpid(),count, line))
        count += 1

def just_wait_and_print_len_and_idx(data, i):
    """Waits for 5 seconds and prints df length and first and last index"""
    # Waste some CPU cycles
    print("process start")
    for line in data[i]:
        print("Process {}, Line: {}".format(os.getpid(), line))

    


def chunkDataset(data, i, chunk_size):
    start = i * chunk_size
    end = start + chunk_size
    return data.iloc[start:end].copy()

if __name__ == '__main__':
    # Constants
    NUM_WORKERS = 6
    data = pd.read_csv("customer_orders.csv")
    npdata = data.to_numpy()

    splits = []
    for i in range(1,NUM_WORKERS):
        splits.append((len(npdata)//NUM_WORKERS)*i)

    splt = np.split(npdata, splits)
    startTime = time.time()
    chunk_size = len(data) // NUM_WORKERS
    workers = []

    for i in range(NUM_WORKERS):
        p = Process(target=just_wait_and_print_len_and_idx, args=(splt, i),)
        p.start()
        workers.append(p)
    
    #wait for workers to finish
    for p in workers:
        p.join()


    endtime = time.time()

    print("All Complete")
    print("Time Taken: {}".format(endtime - startTime))

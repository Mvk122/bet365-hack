import os
import pandas as pd
import numpy as np
import multiprocessing as mp
import time
from multiprocessing import shared_memory, pool


def worker(wData):
    count = 0
    print("Worker {}".format(os.getpid()))
    print("Data length: {}".format(len(wData)))
    for line in wData:
        print("Worker {}, Line {}: {}".format(os.getpid(),count, line))
        count += 1

def just_wait_and_print_len_and_idx(shm, first_idx, last_idx):
    """Waits for 5 seconds and prints df length and first and last index"""
    #get np array from shared memory
    idx_values = data.index.values
    length = len(data)
    pid = os.getpid()

    # Waste some CPU cycles
    time.sleep(1)

    # Print the info
    print('First idx {}, last idx {} and len {} '
          'from process {}'.format(first_idx, last_idx, length, pid))

def chunkDataset(data, i, chunk_size):
    start = i * chunk_size
    end = start + chunk_size
    return data.iloc[start:end].copy()

if __name__ == '__main__':
    # Constants
    NUM_WORKERS = mp.cpu_count()
    # data = pd.read_csv("customer_orders.csv")
    data = pd.read_csv("customer_orders.csv")
    npdata = data.to_numpy()
    np.split(npdata, NUM_WORKERS)
    print(npdata[:10])
    print(type(npdata))
    # add data to shared memory
    # shm = shared_memory.SharedMemory(create=True, size=npdata.nbytes) #create shared memory
    # shmdf = np.ndarray(data.shape, dtype=data.dtypes, buffer=shm.buf) #create np array in shared memory
    # shmdf[:] = data[:] #copy data to shared memory

    startTime = time.time()
    chunk_size = len(data) // NUM_WORKERS

    ctx = mp.get_context('spawn')
    pool = pool.Pool(processes=NUM_WORKERS)


    workers = []

    for i in range(NUM_WORKERS):
        start = i * chunk_size
        # print("start: {}".format(start))
        end = start + chunk_size
        # print("end: {}".format(end))
        worker_data = chunkDataset(data, i, chunk_size)
        p = mp.Process(target=just_wait_and_print_len_and_idx, args=(shared_memory.SharedMemory(name=shm.name), start, end),)
        p.start()
        workers.append(p)
    
    #wait for workers to finish
    for p in workers:
        p.join()


    endtime = time.time()

    print("All Complete")
    print("Time Taken: {}".format(endtime - startTime))

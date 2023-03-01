from multiprocessing import Process
import os
import pandas as pd
import numpy as np
import time
import db
import cProfile


def workerthing(data, i):
    con = db.default_connection()
    cur = con.cursor()
    for line in data[i]:
        cur.execute(f"INSERT INTO what(userz, item, order_date) VALUES ('{line[0]}', '{line[1]}', '{line[2]}')")
    con.commit()



def chunkDataset(data, i, chunk_size):
    start = i * chunk_size
    end = start + chunk_size
    return data.iloc[start:end].copy()

def main():
    # Constants
    NUM_WORKERS = 4
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
        p = Process(target=workerthing, args=(splt, i),)
        p.start()
        workers.append(p)
    
    #wait for workers to finish
    for p in workers:
        p.join()


    endtime = time.time()

    print("All Complete")
    print("Time Taken: {}".format(endtime - startTime))


if __name__ == '__main__':
    cProfile.run('main()')

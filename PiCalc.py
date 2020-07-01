from multiprocessing import Queue, Pool
from decimal import Decimal, getcontext
import time
import functions


num = functions.number_Of_Process

if __name__ == "__main__":
    startTime = time.time()
    lst = []
    with Pool(num) as p:
        lst = p.map(functions.bbp2, ([i for i in range(num)]))

    finishTime = time.time()
    proctime = finishTime - startTime

    getcontext().prec = 10000
    res = Decimal(0)
    for i in lst:
        res += i

    print(res)
    print(f"time : {proctime} ms")


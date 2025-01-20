import threading
import multiprocessing
from queue import Queue
import time
from decimal import Decimal
from decimal import getcontext

def factorial(k):
    if k == 0:
        return 1
    else:
        return k * factorial(k-1)
def e_serie_part(k_start, k_end, que=None):
    getcontext().prec = 100
    partial_sum = 0

    for k in range(k_start, k_end):
            partial_sum += 1 / factorial(k)

    if que is not None:
        que.put(partial_sum)
    else:
        return partial_sum



qres = Queue()

N = 1000
threads_count = 4

num_cores = multiprocessing.cpu_count()
print(f"Number of cores: {num_cores}")
#
# getcontext().prec = 100
#
start_time = time.time()

# pool = multiprocessing.Pool(num_cores)
# results = pool.starmap(pi_serie_part, [(N*k+1, N*(k+1)) for k in range(threads_count)])
#
# for r in results:
#     qres.put(r)

# pi_serie_part(1, 2*N, qres)

thread_list = []
for i in range(threads_count):
    start = N * i + 1
    end = N * (i + 1)
    
    # Calculate the size of the current chunk
    chunk_size = N // (2 ** i)  # Each chunk gets half the size of the previous one
    
    # Adjust the end of the chunk based on the calculated chunk_size
    end = start + chunk_size - 1
    
    # Ensure the end doesn't exceed the original total (N * threads_count)
    end = min(end, N * threads_count)
    
    t = threading.Thread(target=e_serie_part, args=(start, end, qres))
    thread_list.append(t)
    t.start()

for t in thread_list:
    t.join()

end_time = time.time()

print(f"Threads finished. Elapsed time: {end_time - start_time}. {qres.qsize()} elements in queue.")

e_approx = 0
while not qres.empty():
    e_approx += qres.get()


print(f"e approximation: {e_approx}")
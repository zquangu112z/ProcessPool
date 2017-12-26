import time
import multiprocessing
from utils import check_website
from websites import WEBSITE_LIST

NUM_WORKERS = 4

start_time = time.time()

with multiprocessing.Pool(processes=NUM_WORKERS) as pool:
    results = pool.map_async(check_website, WEBSITE_LIST)
    results.wait()

end_time = time.time()

print("Time for MultiProcessingSquirrel: %ssecs" % (end_time - start_time))

'''
Time for MultiProcessingSquirrel: 23.37708830833435sec
python multiprocessing_squirrel.py  0.47s user 0.05s system 2% cpu 23.612 total
'''

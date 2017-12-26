import time
import concurrent.futures
from utils import check_website
from websites import WEBSITE_LIST

NUM_WORKERS = 4

start_time = time.time()

with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:
    futures = {executor.submit(check_website, address)
               for address in WEBSITE_LIST}
    concurrent.futures.wait(futures)

end_time = time.time()

print("Time for FutureSquirrel: %ssecs" % (end_time - start_time))

'''
Time for FutureSquirrel: 5.353148698806763secs
python future_squirrel.py  0.36s user 0.03s system 7% cpu 5.523 total
'''

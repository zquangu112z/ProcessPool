import time
from utils import check_website
from websites import WEBSITE_LIST

start_time = time.time()

for address in WEBSITE_LIST:
    check_website(address)

end_time = time.time()

print("Time for SerialSquirrel: %ssecs" % (end_time - start_time))


'''
Log:
WARNING:root:Timeout expired for website http://really-cool-available-domain.com
WARNING:root:Timeout expired for website http://another-really-interesting-domain.co
WARNING:root:Website http://live.com returned status_code=405
WARNING:root:Website http://netflix.com returned status_code=405
WARNING:root:Website http://bing.com returned status_code=405
Time for SerialSquirrel: 17.2831699848secs
'''

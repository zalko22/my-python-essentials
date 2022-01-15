# Clock that resets after a given amount of seconds

import time

start = True

start_time = time.time()

# Change time_limit to change how long you want the clock to go before reseting
time_limit = 5

while start:

    elapsed_time = time.time() - start_time

    if elapsed_time > time_limit:
        start_time = time.time() - 0
    
    clock = int(elapsed_time)

    # Delete this if you dont want and output of the clocks time
    print(clock)

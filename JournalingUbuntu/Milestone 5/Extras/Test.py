'''
import time

start = time.time(0)
print("Timer test: 30 seconds")
end = time.time(30)
print(end - start)
'''
Timer = int 
# Start timer
my_timer = Timer(60)

# ... do something

# Get time string:
time_hhmmss = my_timer.get_time_hhmmss(1)
print("Time elapsed: %s" % time_hhmmss )
'''
# ... use the timer again
my_timer.restart(60)

# ... do something

# Get time:
time_hhmmss = my_timer.get_time_hhmmss()

# ... etc
'''
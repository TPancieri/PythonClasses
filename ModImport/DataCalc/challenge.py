import time
from time import perf_counter, monotonic, process_time

# time(), perf_counter, monotonic() and process_time()

print("Time clock")
print(time.get_clock_info('time'))
print(time.localtime().tm_hour )
print(time)
print("Perf Counter")
print(time.get_clock_info('perf_counter'))
print(perf_counter())
print("Monotonic")
print(time.get_clock_info('monotonic'))
print(monotonic())
print("Process Time")
print(time.get_clock_info('process_time'))
print(process_time())

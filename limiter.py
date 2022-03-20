from time import time
from collections import deque

class limiter:
    def __init__(self, number_of_calls, limit):
        self.calls = deque([-float('inf')]*number_of_calls,number_of_calls)
        self.limit = limit

    def __call__(self, function):
        def wrapper(*args, **kwargs):
            current_time = time()
            if current_time-self.calls[0]<self.limit:
                print(current_time, 'skipping')
            else:
                function(*args, **kwargs)
                self.calls.append(current_time)
        return wrapper


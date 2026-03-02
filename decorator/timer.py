import time
from datetime import datetime


def timer(func):
    def wrapper(*args, **kwargs):
        # CR: datetime is a bit overkill for this, I would use time.time instead
        #   sidenote - time.perf_counter is used if you want to profile (just cool to know)
        start = datetime.now()
        val = func(*args, **kwargs)
        end = datetime.now()
        print(f"Function took to run: {(end - start).total_seconds()}s")
        return val
    return wrapper


@timer
def hello():
    time.sleep(1)
    print("nah")


hello()

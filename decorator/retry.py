import random


def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                try:
                    val = func(*args, **kwargs)
                except Exception:
                    continue
                else:
                    return val
            return None
        return wrapper
    return decorator

@retry(times=10)
def hello():
    x = random.random()
    if x < 0.1:
        return 6
    else:
        raise Exception


print(hello())
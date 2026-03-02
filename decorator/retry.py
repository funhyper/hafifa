import random


# CR: typing
def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # CR: nice use of _  :)
            for _ in range(times):
                try:
                    val = func(*args, **kwargs)
                except Exception:
                    continue
                else:
                    return val
            return None     # CR: how about raising the exception (if it failed even after the retry I'll want to know)
        return wrapper
    return decorator


@retry(times=10)
# CR: return type `-> None`
def hello():
    x = random.random()
    if x < 0.1:
        return 6
    else:
        raise Exception


print(hello())
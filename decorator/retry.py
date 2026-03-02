import random
from collections.abc import Callable
from typing import Any


def retry(times: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Any:
            for _ in range(times - 1):
                try:
                    val = func(*args, **kwargs)
                except Exception:
                    continue
                else:
                    return val
            return func(*args, **kwargs)

        return wrapper

    return decorator


@retry(times=10)
def hello() -> int:
    x = random.random()
    if x < 0.1:
        return 6
    else:
        raise Exception


def main():
    print(hello())


if __name__ == "__main__":
    main()

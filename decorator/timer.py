import time
from typing import Callable, Any


def timer(func) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        start = time.perf_counter()
        val = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Function took to run: {(end - start)}s")
        return val

    return wrapper


@timer
def hello() -> None:
    time.sleep(1)
    print("nah")


def main():
    hello()


if __name__ == "__main__":
    main()

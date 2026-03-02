# CR: typing!
from collections.abc import Generator


def fibo() -> Generator[int]:
    yield 0
    yield 1
    a, b = 0, 1
    while True:
        yield a + b
        a, b = b, a + b


if __name__ == "__main__":
    fibo_seq = fibo()
    count = 0
    for count, fib_seq_number in enumerate(fibo_seq):
        if count > 10:
            break
        print(fib_seq_number)

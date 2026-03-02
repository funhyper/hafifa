def fibo():
    yield 0
    yield 1
    a = 0
    b = 1
    while True:
        yield a + b
        temp = a
        a = b
        b = temp + b

fibo_seq = fibo()
count = 0
for i in fibo_seq:
    print(i)
    count += 1
    if count == 10:
        break
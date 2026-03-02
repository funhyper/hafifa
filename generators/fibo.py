# CR: typing!
def fibo():
    yield 0
    yield 1
    # CR: you can also write this in one line (not that one line is better) `a, b = 0, 1`
    a = 0
    b = 1
    while True:
        yield a + b
        # CR: in python you can simply do `a, b = b, a + b`
        temp = a
        a = b
        b = temp + b


# CR: dont put code in module level, cuz then if someone imports this file it will run the code, which usually is unwanted
#   use `if __name__ == '__main__':` (you can just type `main` and pycharm will autocomplete)
fibo_seq = fibo()
# CR: can you think of a more pythonic way to do this? hint: enumerate
count = 0
# CR: variable names! what is i?
for i in fibo_seq:
    print(i)
    count += 1
    if count == 10:
        break

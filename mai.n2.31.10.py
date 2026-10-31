def f():
    n = 1
    while True:
        yield n
        n += 1

for i in f():
    print(i)
    if i == 30:
        break
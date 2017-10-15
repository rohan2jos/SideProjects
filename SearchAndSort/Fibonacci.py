def fib(n):

    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def mainFunc():
    arr = []
    for i in range(0, 5):
        arr.append(fib(i))
    return arr


mainFunc()
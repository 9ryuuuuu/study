n = int(input())


def fib(n: int):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(n))

# def generatorfun():
#     yield 1
#     yield 2
#     yield 3

# x = generatorfun()
# print(next(x))
# print(next(x))

def fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b
x = fib(5)

for i in fib(10):
    print(i)
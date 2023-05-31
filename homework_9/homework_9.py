
def fibonacci(n):
    n = input("Enter a number of fibonacci element: ")
    n = int(n)
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

data = list(fibonacci(10))
print(data)

n = int(input("Введіть номер елемента у послідовності Фібоначчі: "))
def fibonacci(n):
    a = 1
    b = 0
    for _ in range(n):
        c = a + b
        a = b
        b = c
        yield b
for d in fibonacci(n):
    value = d
print(value)


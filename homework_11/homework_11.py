"""
Написати власний декоратор, задачею якого має бути друк назви функції i часу, коли вона була викликана. Декоратор має працювати для різних функцій однаково.

Написати кастомний Exception клас, MyCustomException, який має повідомляти "Custom exception is occured".

Написати власний менеджер контексту, задачею якого буде друкувати "=========="  10 знаків дорівнює перед виконанням коду та після виконання коду, таким чином виділяючи блок коду символами дорівнює.

Y випадку виникнення будь-якої помилки вона має бути надрукована текстом, проте програма не має завершити своєї роботи.

Написати конструкцію try ... except ... else ... finally, яка буде робити точно те ж, що i менеджер контексту із попереднього завдання.
"""

#(1)

import time

def decorator(func):
    def wrapper():
        print("current time is:", time.strftime('%H'':''%M'))
        func()
    return wrapper

@decorator
def show():
    print("name of this function is \"show\"")    
show()


#(3)
class custom_exception:
    def __init__(self, value):
        self.value = value
    def __enter__(self):
        print("==========")
    def __exit__(self, type, value, trace):
        print("==========")

with custom_exception(1) as some_value:
    try:
        n = input("enter a number: ")
        n = int(n)
        print("its ok")
    except Exception:
        print("this is not a number")
        print("Custom exception is occured")
        

#(4)
print("write a number \"12345\" to skip this part of program")
while True:
    
    try:
        a = int(input("Enter a something number: "))
        if a == 12345:
            break
    except Exception:
        print(f"this is a {Exception} exception")


#(5)


with custom_exception(1) as some_value:
    try:
        print(x)
    except:
        print("Something went wrong")
    else:
        print("Something went wrong, but we are going to handle it")
    finally:
        print("hello lector!")

#(2)

class MyCustomException(Exception):
    pass
raise MyCustomException("Custom exception is occured")






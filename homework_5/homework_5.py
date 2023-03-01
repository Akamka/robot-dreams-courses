txt = input("Введіь текст: ")

for i in txt:
    if i.isdigit():
        if int(i) % 2 == 0:
            print(f'Ця число {i} - парне')
        else:
            print(f'Ця число {i} - непарне')
    elif i.isalpha():
        if i.islower():
            print(f'Ця буква {i} - маленька')
        else:
            print(f"Ця буква {i} - велика")
            
    else:
        print("це символ")
        
import time

while True:
    print("I love Python")
    time.sleep(4.2)
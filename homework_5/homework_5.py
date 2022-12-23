a = input("enter the text: ")
#number is even or odd
if a.isdigit() is True:
    
    if int(a) % 2 == 0:
        print(f"number:{a} - is even" )
    else:
        print(f"number:{a} - is odd")
                
#string have a small latter or capital
elif a.isalpha() is True:
    if a.isupper():
        print(f"text: {a} - have a capital letter ")
    elif a.islower():
        print(f"text: {a} - have a small letter")

else: 
    print(f"{a} - its a symbol")
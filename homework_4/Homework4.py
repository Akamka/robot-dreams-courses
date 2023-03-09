a = input("enter the text: ")

if a.isdigit() is True:
    
    if int(a) % 2 == 0:
        print("this is number is even" )
    else:
        print("this is number is not even")
        
elif a.isalpha() is True:
    
    print("this is a word and it has",len(a) ,"symbols")
else: 
    print("its not a strint or number")



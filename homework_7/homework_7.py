# stats: кількість записів
# add: додати запис
# delete <name>: видалити запис за іменем (ключем)
# list: список всіх імен в книзі
# show <name>: детальна інформація по імені

#Записи не мають повторюватися, заборонено перезаписувати записи, тільки видаляти і додавати заново. 
print("=====================")
print("write one of this comands:\n\nstats: кількість записів\nadd: додати запис\ndelete <name>: видалити запис за іменем (ключем)\nlist: список всіх імен в книзі\nshow <name>: детальна інформація по імені")
print("=====================")

phonebook = {}
while True:
    user_command = input("Enter a command: ")
    
    if user_command == "exit":
        break
    
      #===================================add
    if user_command == "add" or user_command == "Add":
       key = input("Enter a name: ")
       if phonebook is not None :
           phonebook[key] = input("Enter a phone number: ")
           
           
       
    #===================================delete
    elif user_command == "delete":
            value2 = input("Enter a name that you are want to delete: ")
            if value2 in phonebook:
                del phonebook[value2]
            else: 
                print("Error: no matches")
            
               
    #===================================status
    elif user_command == "stats":
            print(len(phonebook))
            
            
    #===================================list
    elif user_command == "list":
        print(phonebook.keys())
        
        
    #===================================show
    elif user_command == "show":
        name = input("Write finding name: ")
        if name in phonebook:
            print(phonebook.get(name))   
    
    

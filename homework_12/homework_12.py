import json
phonebook = {}  

def write():
    with open('js_file', 'w+') as file:
        data = json.dumps(phonebook)
        file.write(data)



try:
    with open('js_file', 'r') as file:
            data = file.read()
            phonebook = json.loads(data)
except:
    phonebook = {}    

    
def stats():
    
    print("Total number of contacts:", len(phonebook))

def add():
    
    name = input("Enter the name: ")
    if name not in phonebook:
        phone = input("Enter the phone number: ")
        phonebook[name] = {"phone": phone}
        write()
        print(name, "has been added to the phone book.")
    else:
        print(name, "already exists in the phone book.")

def delete(name):
    
    if name in phonebook:
        
        del phonebook[name]
        write()
        print(name, "has been deleted from the phone book.")
    else:
        print(name, "does not exist in the phone book.")

def list():
    
    if phonebook:
        
        print("List of names:")
        for name in phonebook:
            print(name)
    else:
        print("The phone book is empty.")

def show(name):
    
    
    if name in phonebook:
        print("Phone:", phonebook[name])
    else:
        print(name, "does not exist in the phone book.")

# основний цикл програми
while True:
    

    
        
    command = input("Enter command (stats, add, delete, list, show, exit): ")
    if command == "stats":
        stats()
    elif command == "add":
        add()
    elif command == "delete":
        delete(name=input("Searching name: "))
    elif command == "list":
        list()
    elif command == "show":
        show(name=input("Searching name: "))
    elif command == "exit":
        break 
    else:
        print("Invalid command. Please try again.")
        
    
        
      
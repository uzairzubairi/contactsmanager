#!/usr/bin/env python3

def displayCommandMenu():
    print("Contact Manager\n")
    print("COMMAND MENU")
    print("list - display all contacts")
    print("view - view a contact")
    print("add - add a contact")
    print("del - delete a contact")
    print("exit - exit program")

def listFunc(cl):
    for i in range(len(cl)):            #loops through the entire array
        print(f"{i+1}. {cl[i][0]}")     #prints the names of all the contacts

def view(cl):
    num=int(input("Number: "))
    print(f"Name: {cl[num-1][0]}")  #prints the name, email and phone at the number given by the user
    print(f"Email: {cl[num-1][1]}")
    print(f"Phone: {cl[num-1][2]}")

def add(cl):
    name=input("Name: ")
    email=input("Email: ")
    phone=input("Phone: ")
    tempList=[name, email, phone]
    cl.append(tempList)             #adds the newly given info to the array
    print(f"{name} was added.")

def delFunc(cl):
    num=int(input("Number: "))
    deletedStuff=cl.pop(num-1)      #deletes the element at the user's given number
    print(f"{deletedStuff[0]} has been deleted.")


def main():
    contactList=[["Guido van rossum", "abcc@xyz.com","1234567"], 
    ["Eric Idle", "eric@ericidle.com", "+44 20 7946 0958"]]
    cont=True
    displayCommandMenu()
    while cont == True:
        command=input("\nCommand: ")
        if command=="list":
            listFunc(contactList)
        elif command=="view":
            view(contactList)
        elif command=="add":
            add(contactList)
        elif command=="del":
            delFunc(contactList)
        elif command=="exit":
            cont=False
    print("Bye!")

    
if __name__ == "__main__":
    main()

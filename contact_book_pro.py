


import pandas as pd
import os
print("""
    ====================
       Contact Book
    ====================
      
 Add Contact         enter---> 1
 Show Contacts       enter---> 2
 Search Contact      enter---> 3
 Update Contact      enter---> 4
 Delete Contact      enter---> 5
 Total Contacts      enter---> 6
 Exit                enter---> 7
""")
contacts = {} 

if os.path.exists("contacts.csv"):
    df = pd.read_csv("contacts.csv")
    for _, row in df.iterrows():
        contacts[row["Name"]] = row["Number"]
    print("✅ Contacts loaded!")

while True:

    option = input("Choose : ")
    if option == "1":
        name = input("""Add Contact
    add name : """)
        number = input("    add Number : ")
        contacts[name] = number  
        df = pd.DataFrame(contacts.items(), columns=["Name", "Number"])
        df.to_csv("contacts.csv", index=False)
        print("✅ Contact added & saved!")

    elif option == "2":
        show = input("Show all Contacts? (yes/no) : ")
        if show == "yes":
            if len(contacts) == 0:     
                print("❌ this name of contact You deleted   .!")
            else:
                for key, value in contacts.items():
                    print("")
                    print("name :", key)
                    print("number :", value)
                    

    elif option =="3":
        search = input("search contact name :")
        if search in contacts:
                print("Number:", contacts[search])
        else:
            print("❌ Contact not found")

    elif option == "4":
        name = input("Which contact should be updated? : ")
        if name in contacts:
            new_number = input("New Number: ")
            contacts[name] = new_number  
            print("✅ Updated! new number ")
        else:
            print("❌ Contact not found")

    elif option == "5":
        delete = input("delete contact name: ")
        if delete in contacts:
            del contacts[delete]
            df = pd.DataFrame(contacts.items(), columns=["Name", "Number"])
            df.to_csv("contacts.csv", index=False)  
            print("✅ Deleted!")
        else:
            print("❌ Contact not found ")

    elif option == "6":
        print("Total Contacts:", len(contacts))

    elif option == "7":  
        print("Bye! 👋")
        break




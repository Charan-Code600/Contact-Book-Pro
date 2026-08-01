




import pandas as pd
import os

print("""
           ╔══════════════════════════════════╗
           ║       CONTACT BOOK PRO           ║
           ╚══════════════════════════════════╝

**********************************************************

        Add Contact                     Enter  →  1
        Show Contacts                   Enter  →  2
        Search Contact                  Enter  →  3
        Update Contact                  Enter  →  4
        Delete Contact                  Enter  →  5
        Total Contacts                  Enter  →  6
        Exit                            Enter  →  7

***********************************************************
""")

contacts = {}

if os.path.exists("contacts.csv"):
    try:
        df = pd.read_csv("contacts.csv", dtype={"Number": str})
        if "Name" in df.columns and "Number" in df.columns:
            for _, row in df.iterrows():
                contacts[row["Name"]] = row["Number"]
            print(f"✅ {len(contacts)} contact(s) loaded!")
        else:
            print("⚠️  contacts.csv found but missing 'Name'/'Number' columns — starting fresh.")
    except Exception as e:
        print(f"⚠️  Could not read contacts.csv ({e}) — starting fresh.")


def save_contacts():
    df = pd.DataFrame(contacts.items(), columns=["Name", "Number"])
    df.to_csv("contacts.csv", index=False)


def find_contact(name):
    """Case-insensitive lookup. Returns the actual stored key, or None."""
    name_lower = name.strip().lower()
    for key in contacts:
        if key.lower() == name_lower:
            return key
    return None


while True:
    option = input("\nChoose: ")

    if option == "1":
        print("-" * 36)
        name = input("Add name: ").strip()
        if not name:
            print("❌ Name cannot be empty.")
            continue

        existing = find_contact(name)
        if existing:
            print(f"⚠️  '{existing}' already exists with number {contacts[existing]}")
            overwrite = input("Overwrite it? (yes/no): ").strip().lower()
            if overwrite != "yes":
                print("❌ Cancelled.")
                print("-" * 36)
                continue
            name = existing

        number = input("Add Number: ").strip()
        if not number.isdigit() or len(number) < 7:
            print("❌ Invalid number! Must be digits only, at least 7 digits.")
            print("-" * 36)
            continue

        contacts[name] = number
        save_contacts()
        print(f"✅ Contact '{name}' added & saved!")
        print("-" * 36)

    elif option == "2":
        print("-" * 36)
        if len(contacts) == 0:
            print("❌ No contacts found!")
        else:
            for key, value in contacts.items():
                print(f"Name: {key}  |  Number: {value}")
        print("-" * 36)

    elif option == "3":
        print("-" * 36)
        search = input("Search contact name: ").strip()
        found = find_contact(search)
        if found:
            print(f"✅ {found}: {contacts[found]}")
        else:
            print("❌ Contact not found!")
        print("-" * 36)

    elif option == "4":
        print("-" * 36)
        name = input("Which contact to update?: ").strip()
        found = find_contact(name)
        if found:
            new_number = input("New Number: ").strip()
            if not new_number.isdigit() or len(new_number) < 7:
                print("❌ Invalid number! Must be digits only, at least 7 digits.")
            else:
                contacts[found] = new_number
                save_contacts()
                print(f"✅ '{found}' updated!")
        else:
            print("❌ Contact not found!")
        print("-" * 36)

    elif option == "5":
        print("-" * 36)
        delete = input("Delete contact name: ").strip()
        found = find_contact(delete)
        if found:
            confirm = input(f"Are you sure you want to delete '{found}'? (yes/no): ").strip().lower()
            if confirm == "yes":
                del contacts[found]
                save_contacts()
                print(f"✅ '{found}' deleted!")
            else:
                print("❌ Cancelled.")
        else:
            print("❌ Contact not found!")
        print("-" * 36)

    elif option == "6":
        print("-" * 36)
        print(f"📇 Total Contacts: {len(contacts)}")
        print("-" * 36)

    elif option == "7":
        print("\n👋 Bye!")
        break

    else:
        print("❌ Invalid option! Choose between 1-7.")

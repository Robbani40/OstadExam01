
phonecontacts = {}


def load_from_file():
    try:
        with open('contacts.txt', 'r') as file:
            for line in file:
                name, phone = line.strip().split(': ')
                phonecontacts[name] = phone
    except FileNotFoundError:
        print("No previous contacts found. Starting fresh.")

def save_to_file():
    with open('contacts.txt', 'w') as file:
        for name, phone in phonecontacts.items():
            file.write(f"{name}: {phone}\n")


def add_contact(name, phone):
    phonecontacts[name] = phone
    save_to_file()


def display_contacts():
    if not phonecontacts:
        print("No contacts saved yet.")
    else:
        print("Saved Contacts:")
        for name, phone in phonecontacts.items():
            print(f"{name}: {phone}")

load_from_file()  

while True:
    choice = input("1. Add Contact\n2. View Contacts\n3. Exit\nEnter your choice: ")
    
    if choice == '1':  
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        add_contact(name, phone) 
        display_contacts()  
    elif choice == '3':  
        print("Exiting. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

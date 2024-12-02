phoneNumber = {}

def add_contact(name, phone):
    
    if phone in phoneNumber.values():
        print(f"Error: The phone number {phone} is already assigned to another contact.")
    else:
        
        phoneNumber[name] = phone
        print(f"Contact {name} with phone number {phone} added successfully.")

def display_contacts():
    print("\nCurrent Phonebook:")
    for name, phone in phoneNumber.items():
        print(f"Name: {name}, Phone: {phone}")

# Main program
while True:
    
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter the name: ")
        phone = input("Enter the phone number: ")
        add_contact(name, phone)
    elif choice == '2':
        display_contacts()
    elif choice == '3':
        print("Exiting the program.!")
        break
    else:
        print("Invalid choice. Please try again.")
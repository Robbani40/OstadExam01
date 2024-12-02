# Phone contacts dictionary
phonecontacts = {}

# Function to load contacts from the file when the program starts
def load_from_file():
    try:
        with open('contacts.txt', 'r') as file:
            for line in file:
                name, phone = line.strip().split(': ')
                phonecontacts[name] = phone
    except FileNotFoundError:
        print("No previous contacts found. Starting fresh.")

# Function to save contacts to the file (sorted by name)
def save_to_file():
    with open('contacts.txt', 'w') as file:
        # Sort contacts by name before saving
        for name in sorted(phonecontacts.keys()):
            file.write(f"{name}: {phonecontacts[name]}\n")

# Function to add a new contact and save it
def add_contact(name, phone):
    if not name.isalpha():
        print("Error: Name must be a string (letters only). Please try again.")
        return
    
    if not phone.isdigit():
        print("Error: Phone number must be an integer (digits only). Please try again.")
        return
    
    phonecontacts[name] = phone
    save_to_file()
    print(f"Contact '{name}' added successfully.")

# Function to display all saved contacts (sorted by name)
def display_contacts():
    if not phonecontacts:
        print("No contacts saved yet.")
    else:
        print("Saved Contacts (sorted by name):")
        # Display contacts sorted by name
        for name in sorted(phonecontacts.keys()):
            print(f"{name}: {phonecontacts[name]}")

# Function to remove a contact
def remove_contact(name):
    if name in phonecontacts:
        del phonecontacts[name]
        save_to_file()
        print(f"Contact '{name}' removed successfully.")
    else:
        print(f"No contact found for '{name}'.")

# Function to search for a contact by name or phone number
def search_contact(search_term):
    found_contacts = {name: phone for name, phone in phonecontacts.items() if search_term.lower() in name.lower() or search_term in phone}
    
    if found_contacts:
        print("Found Contacts:")
        for name, phone in sorted(found_contacts.items()):
            print(f"{name}: {phone}")
    else:
        print("No contacts found matching the search term.")

# Main program loop
load_from_file()  # Load contacts from file when the program starts

while True:
    choice = input("1. Add Contact\n2. View Contacts\n3. Remove Contact\n4. Search Contacts\n5. Exit\nEnter your choice: ")
    
    if choice == '1':  # Add contact
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        add_contact(name, phone)  # Add and save the contact
    elif choice == '2':  # View contacts
        display_contacts()  # Display all saved contacts
    elif choice == '3':  # Remove contact
        name = input("Enter the name of the contact to remove: ")
        remove_contact(name)  # Remove the contact and update the file
    elif choice == '4':  # Search contacts
        search_term = input("Enter the name or phone number to search: ")
        search_contact(search_term)  # Search and display matching contacts
    elif choice == '5':  # Exit the program
        print("Exiting. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
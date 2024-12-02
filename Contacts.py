import json

CONTACTS_FILE = "contacts.json"

def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    print("\n--- Add New Contact ---")
    name = input("Enter Name: ").strip()
    if not name:
        print("Name is required!")
        return

    if name in contacts:
        print("Contact already exists!")
        return
    name = input("Enter Name:").strip()
    email = input("Enter Email: ").strip()
    phone = input("Enter Phone Number: ").strip()
    address = input("Enter Address: ").strip()

    if not phone:
        print("Phone Number is required!")
        return

    contacts[name] = {
        "email": email if email else "N/A",
        "phone": phone,
        "address": address if address else "N/A"
    }
    print("Contact added successfully!")


def view_contacts(contacts):
    if not contacts:
        print("\nNo contacts available.")
        return

    print("\n--- Contact List ---")
    for name, details in contacts.items():
        print(f"Name: {name ['name']} ")
        print(f"Email: {details['email']}")
        print(f"Phone: {details['phone']}")
        print(f"Address: {details['address']}")
        print("-" * 20)

# Main menu
def main():
    contacts = load_contacts()

    while True:
        print("0. Name")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            save_contacts(contacts)
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
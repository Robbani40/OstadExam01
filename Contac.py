
phonecontacts = {
    "Alice": "12345",
    "Bob": "67890",
    "Charlie": "54321"
}

def display_contacts():
    if not phonecontacts:
        print("\nNo contacts saved yet.")
    else:
        print("\nSaved Contacts:")
        print("Name       |  Number")
        print("-------------------------")
        for name, phone in phonecontacts.items():
            print(f"{name:<10} | {phone}")

display_contacts()

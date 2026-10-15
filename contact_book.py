import json
import os

FILE_NAME = "contacts.json"


class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone
        }


def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    contact = Contact(name, phone)
    contacts.append(contact.to_dict())
    save_contacts(contacts)
    print("Contact added successfully!")


def search_contact(contacts):
    name = input("Enter name to search: ").lower()

    for contact in contacts:
        if name in contact["name"].lower():
            print(contact["name"], "-", contact["phone"])
            return

    print("Contact not found!")


def update_contact(contacts):
    name = input("Enter name to update: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            contact["name"] = input("Enter new name: ")
            contact["phone"] = input("Enter new phone: ")
            save_contacts(contacts)
            print("Contact updated!")
            return

    print("Contact not found!")


def delete_contact(contacts):
    name = input("Enter name to delete: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted!")
            return

    print("Contact not found!")


def main():
    contacts = load_contacts()

    while True:
        print("\n--- CONTACT BOOK ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
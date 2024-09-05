#Contact Management System

import json

#Function to load contacts from a file
def load_contacts():
    try:
        with open('contacts.json','r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = {}
    return contacts

#Function to save contacts to a file
def save_contacts(contacts):
    with open('contacts.json','w') as file:
        json.dump(contacts, file, indent=4)

#Function to add a new contact
def add_contact(name, phone, contacts):
    if name in contacts:
        print("Contact already exists. Use a different name.")
    else:
        contacts[name]= phone
        save_contacts(contacts)
        print(f"\n {name} has been added to contacts with the phone number: {phone}")

#Function to view all contacts
def view_contacts(contacts):
    if contacts:
        print("\n Contacts:")
        for name, phone in contacts.items():
            print(f"{name}:{phone}")
    else:
        print(" No Contacts to Display")

#Function to search a contact by name
def search_contact(name,contacts):
    if name in contacts:
        print(f"Contact found-{name}:{contacts[name]}")
    else:
        print(f"Contact with name '{name}' not found")

#Function to Update contact information
def update_contact(name,new_phone,contacts):
    if name in contacts:
        contacts[name] = new_phone
        save_contacts(contacts)
        print(f"Contact information for {name} has been updated.")
    else:
        print(f"Contact with name '{name}' not found.")

#Function to delete a contact
def delete_contacts(name,contacts):
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"{name} has been deleted from contacts")
    else:
        print(f"{name} not found in contacts")


def main():
    contacts = load_contacts()
    print("\n CONTACT MANAGEMENT SYSTEM")

    while True:    
        print("\n 1. Add Contact")
        print(" 2. View Contact List")
        print(" 3. Search Contact")
        print(" 4. Update Contact")
        print(" 5. Delete Contact")
        print(" 6. Exit")
        case = input("\n Enter your choice: ")

        if case == "1":
            #Data Validation for name.
            name= input("Enter Name: ")
            if len(name)== 0:
                print("Name cannot be Empty. Contact not added, enter a Name.")
                break

            if name.isnumeric():
                print("Name should only be Alphabets. Enter a Valid Name")
                break

            phone= input("Enter Phone Number: ")
            #Data Validation for Phone Number.
            if phone.isalpha():
                print("Phone Number should contain only Digits. Contact not added.\n Enter a Valid Phone Number")
                break
    
            if len(phone)!= 10:
                print("Phone Number should be 10 Digits only.\n Contact not added, enter a Valid Phone Number")
                break

            add_contact(name,phone,contacts)

        elif case == "2":
            view_contacts(contacts)
        
        elif case == "3":
            name= input("Enter Name to search: ")
            #Data Validation for name.
            if len(name)== 0:
                print("Name cannot be Empty. Contact not added, enter a Name.")
                break

            if name.isnumeric():
                print("Name should only be Alphabets. Enter a Valid Name")
                break
            search_contact(name,contacts)

        elif case == "4":
            name= input("Enter Name to update: ")
            #Data Validation for name.
            if len(name)== 0:
                print("Name cannot be Empty. Contact not added, enter a Name.")
                break

            if name.isnumeric():
                print("Name should only be Alphabets. Enter a Valid Name")
                break

            new_phone= input("Enter New Phone Number: ")
            #Data Validation for phone.
            if new_phone.isalpha():
                print("Phone Number should contain only Digits. Contact not added.\n Enter a Valid Phone Number")
                break
    
            if len(new_phone)!= 10:
                print("Phone Number should be 10 Digits only.\n Contact not added, enter a Valid Phone Number")
                break
            update_contact(name,new_phone,contacts)

        elif case == "5":
            name= input("Enter Name to delete: ")
            #Data Validation for name.
            if len(name)== 0:
                print("Name cannot be Empty. Contact not added, enter a Name.")
                break

            if name.isnumeric():
                print("Name should only be Alphabets. Enter a Valid Name")
                break
            delete_contacts(name,contacts)

        elif case == "6":
            print("Existing the contact Management System")
            break

        else:
            print("Invalid Choice.\n Please Try again.")

if __name__ == "__main__":
    main()
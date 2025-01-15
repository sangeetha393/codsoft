phone_contacts = {}

while (choice := input("\n1.Add a contact  2.View all contacts  3.Search for a contact  4.Update a contact  5.Delete a contact  6.Exit: ")) != "6":
    if choice == "1":
        name = input("Name: ")
        phone_contacts[name] = {
            "Phone": input("Phone number: "),
            "Email": input("Email: "),
            "Address": input("Address: ")
        }
    elif choice == "2":
        if phone_contacts:
            for name, details in phone_contacts.items():
                print(f"Name: {name}, Details: {details}")
        else:
            print("No contacts found.")
    elif choice == "3":
        search_name = input("Search Name: ")
        print(phone_contacts.get(search_name, "Not found."))
    elif choice == "4":
        name = input("Update Name: ")
        if name in phone_contacts:
            phone_contacts[name].update({
                "Phone": input("New Phone: ") or phone_contacts[name]["Phone"],
                "Email": input("New Email: ") or phone_contacts[name]["Email"],
                "Address": input("New Address: ") or phone_contacts[name]["Address"]
            })
            print(f"Contact updated: {phone_contacts[name]}")
        else:
            print("Not found.")
    elif choice == "5":
        delete_name = input("Delete Name: ")
        if delete_name in phone_contacts:
            del phone_contacts[delete_name]
            print(f"Contact '{delete_name}' deleted.")
        else:
            print("Not found.")
    else:
        print("Invalid choice. Please try again.")

print("Goodbye!")
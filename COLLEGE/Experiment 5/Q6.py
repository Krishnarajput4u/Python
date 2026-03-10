contacts = {}

while True:
    print("1.Add 2.Search 3.Update 4.Delete 5.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone

    elif choice == "2":
        name = input("Enter name to search: ")
        print(contacts.get(name, "Not found"))

    elif choice == "3":
        name = input("Name to update: ")
        if name in contacts:
            contacts[name] = input("New phone: ")

    elif choice == "4":
        name = input("Name to delete: ")
        contacts.pop(name, None)

    else:
        break
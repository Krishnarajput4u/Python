tasks = []

while True:
    print("1.Add 2.View 3.Remove 4.Exit")
    choice = input("Choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == "2":
        for t in tasks:
            print(t)

    elif choice == "3":
        task = input("Task to remove: ")
        if task in tasks:
            tasks.remove(task)

    else:
        break

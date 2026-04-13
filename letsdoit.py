tasks = []
while True:
    print("\n   TO DO LIST  ")
    print("1 . VIEW")  
    print("2 . ADD")
    print("3 . DELETE")
    print("4 . EXIT")
    choice = input("Enter your choice : ")
    if choice == "1" :
        if len(tasks) == 0:
            print("NO TASKS FOUND")
        else :
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(i, task)
    elif choice == "2":
        user_add = input( "Enter your task :" )
        tasks.append(user_add)
    elif choice == "3":
        user_delete = int(input("ENTER TASK NUMBER"))
        if user_delete > len(tasks):
            print("INVALID TASK NOT FOUND")
        else:
            i = user_delete - 1
            tasks.pop(i)
            print("DELETED", user_delete)
    elif choice == "4":
        user_exit = input("DO YOU WANT TO EXIT? ")
        user_exit = user_exit.strip().lower()
        if user_exit in ["y", "yes"]:
            break
        else:
            continue
    else:
        print("INVALID CHOICE")


    

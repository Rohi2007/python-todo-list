print("----TO DO LIST----")
task = []
while True:
    print("\n1.Add Tasks")
    print("2.View Tasks")
    print("3.Delete Tasks")
    print("4.Exit")
    option = int(input("Enter your option: "))
    if option == 1:
        new_task = input("Enter the new task: ")
        task.append(new_task)
        print("New Task added successfully")
    elif option == 2:
        if len(task) == 0:
            print("\nNo tasks are present")
        else:
            print("----Your Tasks----")
            for i in range(len(task)):
                print(f"{i+1}. {task[i]}")
    elif option == 3:
        del_task = int(input("Which task you want to delete: "))
        if del_task <= len(task):
            task.pop(del_task - 1)
            print("Task deleted successfully")
        else:
            print("Invalid task number")
    elif option == 4:
        print("Exiting program...")
        break
    else:
        print("Invalid option. Please try again.")
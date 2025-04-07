def main():
    tasks = []

    while True:
        print("Welcome to the App")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark task as Done")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            print()
            n_tasks = int(input("How many tasks you want to add: "))

            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task":task,"done":False})
                print("Task Added")

        elif choice == '2':
            print("\nTasks: ")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {'status'}")

        elif choice == '3':
            task_index = int(input("Enter the task number to mark as done: "))
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("TAsk marked as done")
            else:
                print("Invalid Number, Please Try again")

        elif choice == '4':
            print()
            task_to_delete = input("Enter the task that you want to delete: ")
            
            tasks = [task for task in tasks if task["task"] != task_to_delete]
            print("Task removed")

        elif choice == '5':
            print("Please Enter valid Number")

        else:
            print("Bye See you soon")

if __name__ == "__main__":
  main()
        

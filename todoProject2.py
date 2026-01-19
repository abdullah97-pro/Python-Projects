todos = []

def addTask(task):
    todos.append(task)
    print(f"Added {task}")

def removeTask(task):
    if task in todos:
        todos.remove(task)
        print(f"Removed {task}")
    else:
        print(f"Can not found {task}")

def listTask():
    if not todos:
        print("Not exist")
    else:
        for i, task in enumerate(todos,1):
            print(f"{i}, {task}")

def main():
    while True:
        command = input("Enter command (add, remove, list, quit): ").strip().lower()
        if command == 'add':
            task = input("Task to add: ")
            addTask(task)
        elif command == 'remove':
            task = input("Task to remove: ")
            removeTask(task)
        elif command == 'list':
            listTask()
        elif command == 'quit':
            print("Exiting Todo Manager.")
            break
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()

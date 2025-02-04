class ToDoListApp:
    def __init__(self):
        self.tasks = []

    def display_menu(self):
        print("\nTo-Do List App")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks available.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def update_task(self, task_number, new_task):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' deleted successfully!")
        else:
            print("Invalid task number.")

    def run(self, inputs):
        input_index = 0
        while input_index < len(inputs):
            self.display_menu()
            choice = inputs[input_index]
            input_index += 1

            if choice == "1":
                self.view_tasks()
            elif choice == "2":
                if input_index < len(inputs):
                    task = inputs[input_index]
                    input_index += 1
                    self.add_task(task)
                else:
                    print("No task provided.")
            elif choice == "3":
                if input_index + 1 < len(inputs):
                    task_number = int(inputs[input_index])
                    new_task = inputs[input_index + 1]
                    input_index += 2
                    self.update_task(task_number, new_task)
                else:
                    print("Insufficient data for updating task.")
            elif choice == "4":
                if input_index < len(inputs):
                    task_number = int(inputs[input_index])
                    input_index += 1
                    self.delete_task(task_number)
                else:
                    print("No task number provided.")
            elif choice == "5":
                print("Exiting the app. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Example predefined inputs for testing purposes
    inputs = ["2", "Buy groceries", "2", "Call mom", "1", "3", "1", "Buy milk", "4", "2", "5"]
    app = ToDoListApp()
    app.run(inputs)


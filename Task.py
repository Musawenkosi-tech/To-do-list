from datetime import date

class Task:
    def __init__(self, description):
        self.description = description
        self.date = date.today()
        self.complete_status = False
    
    def mark_complete(self):
        self.complete_status = True
    
    def __str__(self):
        mark = "✅" if self.complete_status else "○"
        return f"{mark} {self.description} ({self.date})"

tasks = []

while True:
    print("="*40)
    print("📋  To do Menu")
    print("="*40)
    print("1. Add Task ➕")
    print("2. View Tasks 📋")
    print("3. Mark Complete✅")
    print("4. Exit")
    print("="*40)
    choice = input("Please pick 1-4: ")
    

    if choice == "1":
        description = input("Please enter task: ")
        new_task = Task(description)
        tasks.append(new_task)
        print("Task added!")
        
    elif choice == "2":
        if not tasks:
            print("😴 No tasks yet!")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
                
    elif choice == "3":
        if not tasks:
            print("😴 No tasks yet!")
        else:
            print("\nWhich task to complete?")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            
            try:
                num = int(input("Enter number: ")) - 1
                if 0 <= num < len(tasks):
                    tasks[num].mark_complete()
                    print("✅ Task marked complete!")
                else:
                    print("❌ Invalid number!")
            except:
                print("❌ Enter a number!")
    
    elif choice == "4":
        print("✨ Thank you for using the app, Goodbye!")
        break
        
    else:
        print("❌Invalid choice!")




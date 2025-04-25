class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"{item} has been pushed onto the stack.")

    def pop(self):
        if self.is_empty():
            print("Stack is empty, cannot pop.")
        else:
            popped_item = self.stack.pop()
            print(f"{popped_item} has been popped from the stack.")

    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print(f"Top element is: {self.stack[-1]}")

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack elements:", self.stack)

def menu():
    stack = Stack()
    while True:
        print("\nMenu:")
        print("1. Push element to stack")
        print("2. Pop element from stack")
        print("3. Peek top element")
        print("4. Check if stack is empty")
        print("5. Display stack")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            item = int(input("Enter the element to push onto the stack: "))
            stack.push(item)
        elif choice == "2":
            stack.pop()
        elif choice == "3":
            stack.peek()
        elif choice == "4":
            print("Stack is empty." if stack.is_empty() else "Stack is not empty.")
        elif choice == "5":
            stack.display()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

menu()

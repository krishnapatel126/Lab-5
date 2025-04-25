class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} has been added to the queue.")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, cannot dequeue.")
        else:
            dequeued_item = self.queue.pop(0)
            print(f"{dequeued_item} has been removed from the queue.")

    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print(f"Front element is: {self.queue[0]}")

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue elements:", self.queue)

def menu():
    queue = Queue()
    while True:
        print("\nMenu:")
        print("1. Enqueue element to queue")
        print("2. Dequeue element from queue")
        print("3. Peek front element")
        print("4. Check if queue is empty")
        print("5. Display queue")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            item = int(input("Enter the element to enqueue to the queue: "))
            queue.enqueue(item)
        elif choice == "2":
            queue.dequeue()
        elif choice == "3":
            queue.peek()
        elif choice == "4":
            print("Queue is empty." if queue.is_empty() else "Queue is not empty.")
        elif choice == "5":
            queue.display()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

menu()

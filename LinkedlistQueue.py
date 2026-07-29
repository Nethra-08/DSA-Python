
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
            print(f"{data} inserted into the queue.")
            return

        self.rear.next = new_node
        self.rear = new_node
        print(f"{data} inserted into the queue.")

    
    def dequeue(self):
        if self.front is None:
            print("Queue is empty!")
            return

        removed = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        print(f"{removed} removed from the queue.")
    def display(self):
        if self.front is None:
            print("Queue is empty!")
            return

        temp = self.front
        print("Queue elements:")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

queue = Queue()
print("\nQueue Operations")
print("1. Enqueue")
print("2. Dequeue")
print("3. Display")
print("4. Exit")


while True:
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter the value to insert: "))
        queue.enqueue(value)

    elif choice == 2:
        queue.dequeue()

    elif choice == 3:
        queue.display()

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please try again.")

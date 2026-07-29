class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self, size):
        self.top = None
        self.size = size
        self.count = 0

    def push(self, value):
        if self.count == self.size:
            print("Stack Overflow")
            return

        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.count += 1
        print(value, "pushed")

    def pop(self):
        if self.top is None:
            print("Stack Underflow")
            return

        value = self.top.data
        self.top = self.top.next
        self.count -= 1
        print(value, "popped")

    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Top element:", self.top.data)

    def display(self):
        if self.top is None:
            print("Stack is empty")
            return

        temp = self.top
        print("Stack elements:")
        while temp:
            print(temp.data)
            temp = temp.next


size = int(input("Enter stack size: "))

stack = Stack(size)
print("\n--- Stack functions ---")
print("1. Push")
print("2. Pop")
print("3. Peek")
print("4. Display")
print("5. Exit")

while True:
    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        stack.push(value)

    elif choice == 2:
        stack.pop()

    elif choice == 3:
        stack.peek()

    elif choice == 4:
        stack.display()

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice")

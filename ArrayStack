class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size

    def push(self, value):
        if len(self.stack) == self.size:
            print("Stack Overflow")
        else:
            self.stack.append(value)
            print(value, "pushed")

    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow")
        else:
            print(self.stack.pop(), "popped")

    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Top element:", self.stack[-1])

    def display(self):
        print("Stack:", self.stack)


size = int(input("Enter stack size: "))
s = Stack(size)
print("\n--- Stack Menu ---")
print("1. Push")
print("2. Pop")
print("3. Peek")
print("4. Display")
print("5. Exit")

while True:
    choice = int(input("\nEnter your choice: "))

    match choice:
        case 1:
            value = int(input("Enter value: "))
            s.push(value)

        case 2:
            s.pop()

        case 3:
            s.peek()

        case 4:
            s.display()

        case 5:
            print("Exiting...")
            break

        case _:
            print("Invalid choice")

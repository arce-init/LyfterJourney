class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:

    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data, self.top)
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return None
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data

    def print_structure(self):
        current_node = self.top
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

stack = Stack()
stack.push("First")
stack.push("Second")
stack.push("Third")

stack.print_structure()

removed = stack.pop()
print(f"Removed: {removed}")

stack.print_structure()
class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


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


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_left(self, data):
        new_node = Node(data, next=self.head, prev=None)
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def push_right(self, data):
        new_node = Node(data, next=None, prev=self.tail)
        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node
        if self.head is None:
            self.head = new_node

    def print_structure(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


def get_length(start_node):
    count = 0
    current_node = start_node
    while current_node is not None:
        count += 1
        current_node = current_node.next
    return count


def bubble_sort(start_node):
    length = get_length(start_node)

    for outer_index in range(length - 1):
        has_made_changes = False
        current_node = start_node

        for index in range(length - 1 - outer_index):
            next_node = current_node.next

            if current_node.data > next_node.data:
                current_node.data, next_node.data = next_node.data, current_node.data
                has_made_changes = True

            current_node = current_node.next

        if not has_made_changes:
            return


print("=== Stack ===")
stack = Stack()
stack.push("Third")
stack.push("First")
stack.push("Second")

bubble_sort(stack.top)
stack.print_structure()

print("\n=== Deque ===")
deque = Deque()
deque.push_right("C")
deque.push_right("A")
deque.push_right("B")

bubble_sort(deque.head)
deque.print_structure()
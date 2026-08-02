class Node:

    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

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

    def pop_left(self):
        if self.head is None:
            print("Deque is empty")
            return None
        removed_node = self.head
        self.head = removed_node.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None

            return removed_node.data

    def pop_right(self):
        if self.tail is None:
            print("Deque is empty")
            return None
        removed_node = self.tail
        self.tail = removed_node.prev
        if self.tail.next is not None:
            self.tail.next = None
        else:
            self.head = None
        return removed_node.data

    def print_structure(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


deque = Deque()
deque.push_right("B")
deque.push_right("C")
deque.push_left("A")

deque.print_structure()

removed_left = deque.pop_left()
removed_right = deque.pop_right()

print(f"Removed left: {removed_left}")
print(f"Removed right: {removed_right}")

deque.print_structure()
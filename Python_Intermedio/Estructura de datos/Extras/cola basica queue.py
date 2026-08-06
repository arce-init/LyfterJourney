class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            print("Queue is empty")
            return None
        removed_node = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return removed_node.data

    def print_all(self):
        current_node = self.head
        elements = ""
        while current_node is not None:
            if current_node.next is not None:
                elements += f"{current_node.data} -> "
            else:
                elements += f"{current_node.data}"
            current_node = current_node.next
        print(elements)


q = Queue()

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

q.print_all()

result = q.dequeue()
print(result)

q.print_all()
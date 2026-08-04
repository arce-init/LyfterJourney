class Node:

    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data, next=None, prev=self.tail)
        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node
        if self.head is None:
            self.head = new_node

    def prepend(self, data):
        new_node = Node(data, next=self.head, prev=None)
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def delete(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next

                if current_node.next is not None:
                    current_node.next.prev = current_node.prev
                else:
                    self.tail = current_node.prev
                return
            current_node = current_node.next
        print(f"{data} not found in the list")

    def print_forward(self):
        current_node = self.head
        elements = ""
        while current_node is not None:
            if current_node.next is not None:
                elements += f"{current_node.data} -> "
            else:
                elements += f"{current_node.data}"
            current_node = current_node.next
        print(elements)

    def print_backward(self):
        current_node = self.tail
        elements = ""
        while current_node is not None:
            if current_node.prev is not None:
                elements += f"{current_node.data} -> "
            else:
                elements += f"{current_node.data}"
            current_node = current_node.prev
        print(elements)


dll = DoublyLinkedList()

dll.append("A")
dll.append("B")
dll.append("C")

dll.print_forward()
dll.print_backward()

dll.prepend("X")
dll.print_forward()
dll.print_backward()

dll.delete("B")
dll.print_forward()
dll.print_backward()
class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def insert_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def delete(self, data):
        if self.head is None:
            print("List is empty")
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

        print(f"{data} not found in the list")

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


ll = LinkedList()

ll.insert_front(10)
ll.insert_front(20)
ll.print_all()

ll.insert_back(30)
ll.print_all()

ll.delete(10)
ll.print_all()
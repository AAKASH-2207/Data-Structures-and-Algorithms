# prompt: code for linked list with comment at each line

# A Node class that contains data and a reference to the next node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# A LinkedList class that contains a head node and methods for inserting, deleting, and traversing the list
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert a new node at the beginning of the list
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert a new node at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    # Delete a node from the beginning of the list
    def delete_at_beginning(self):
        if self.head is None:
            return
        self.head = self.head.next

    # Delete a node from the end of the list
    def delete_at_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
        else:
            current_node = self.head
            while current_node.next.next is not None:
                current_node = current_node.next
            current_node.next = None

    # Traverse the list and print the data of each node
    def traverse(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

# Create a new linked list
linked_list = LinkedList()

# Insert some nodes into the list
linked_list.insert_at_beginning(1)
linked_list.insert_at_end(2)
linked_list.insert_at_beginning(3)
linked_list.insert_at_end(4)

# Traverse the list
linked_list.traverse()

# Delete a node from the beginning of the list
linked_list.delete_at_beginning()

# Delete a node from the end of the list
linked_list.delete_at_end()

# Traverse the list again
linked_list.traverse()

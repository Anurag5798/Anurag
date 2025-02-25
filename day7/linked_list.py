class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_pos(self, data, pos):
        new_node = Node(data)
        if pos <= 1 or self.head is None:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        count = 1
        while current is not None and count < pos - 1:
            current = current.next
            count += 1
        if current is None:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            new_node.next = current.next
            current.next = new_node

    def delete_at_pos(self, pos):
        if self.head is None:
            print("List is empty")
            return
        if pos <= 1:
            self.head = self.head.next
            return
        current = self.head
        count = 1
        while current is not None and count < pos - 1:
            current = current.next
            count += 1
        if current is None or current.next is None:
            print("Position out of bounds")
            return
        current.next = current.next.next

    def display_reverse(self):
        def _display_reverse(node):
            if node is None:
                return
            _display_reverse(node.next)
            print(node.data, end=" -> ")
        _display_reverse(self.head)
        print("None")

if __name__ == "__main__":
    ll = LinkedList()
    while True:
        print("\nLinked List Operations:")
        print("1. Add at position")
        print("2. Delete at position")
        print("3. Display list in reverse")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = int(input("Enter data (integer): "))
            pos = int(input("Enter position (1-indexed): "))
            ll.add_at_pos(data, pos)
        elif choice == 2:
            pos = int(input("Enter position (1-indexed) to delete: "))
            ll.delete_at_pos(pos)
        elif choice == 3:
            print("Linked List in Reverse:")
            ll.display_reverse()
        elif choice == 4:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

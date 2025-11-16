class Node:
    """
    An individual node in the linked list.
    Stores the data and a reference (pointer) to the next node.
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    """
    The main LinkedList structure.
    Manages the head of the list and provides list operations.
    """
    def __init__(self):
        self.head = None
        self.size = 0
        
    def __len__(self):
        """Allows use of len(linked_list)"""
        return self.size
    
    def __str__(self):
        """Allows use of print(linked_list)"""
        return f"LinkedList(size={self.size})"
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
    
    def is_empty(self):
        """Checks if the list is empty."""
        return self.head is None
    
    def insert_at_beginning(self, data):
        """Adds a new node to the front of the list (O(1))."""
        new_node = Node(data)
        new_node.next = self.head  # New node's next is the old head
        self.head = new_node        # List's head is now the new node
        self.size += 1
        
    def append(self, data):
        """Adds a new node to the end of the list (O(n))."""
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            self.size += 1
            return

        current = self.head
        # Traverse to the last node
        while current.next:
            current = current.next

        current.next = new_node
        self.size += 1
        
    def delete(self, key):
        """Deletes the first node found with the matching key (O(n))."""
        
        curr = self.head
        
        # Case 1: Key is in the head node
        if curr and curr.data == key:
            self.head = curr.next
            self.size -= 1
            return
        
        # Case 2: Key is in a middle or last node
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
            
        if curr is None:
            return f'{key} not found in the list'
        
        prev.next = curr.next
        self.size -= 1
                
                
if __name__ == '__main__':
    # 1. Initialize the list
    my_list = LinkedList()

    # 2. Insert and append elements
    my_list.insert_at_beginning(10)  # List: [10]
    my_list.append(20)               # List: [10, 20]
    my_list.insert_at_beginning(5)   # List: [5, 10, 20]
    my_list.append(30)               # List: [5, 10, 20, 30]

    # 3. Use Pythonic features
    print(my_list)                   # Output: LinkedList(size=4)
    print(f"Size: {len(my_list)}")   # Output: Size: 4

    print("List contents:")
    for item in my_list:             # Iterates through the list
        print(item)
    # Output: 5, 10, 20, 30

    # 4. Delete elements
    my_list.delete(10)               # List: [5, 20, 30]
    print("\nAfter deleting 10:")
    for item in my_list:
        print(item)
    # Output: 5, 20, 30

    my_list.delete(5)                # List: [20, 30]
    my_list.delete(100)              # Output: Key '100' not found in list.
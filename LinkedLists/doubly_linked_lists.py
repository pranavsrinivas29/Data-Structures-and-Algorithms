class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data
        
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def __len__(self):
        return self.size

    def __str__(self):
        return f"DoublyLinkedList(size={self.size})"        
    
    def __iter__(self):
        """Allows iteration (forward traversal)."""
        current = self.head
        while current:
            yield current.data
            current = current.next
               
    def is_empty(self):
        return self.head is None
    
    def insert_at_beginning(self, data):
        """Adds a new node to the front of the list (O(1))."""
        
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
        self.size += 1
        
    def append(self, data):
        """Adds a new node to the end of the list (O(1) because of the tail pointer)."""
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
    
    def delete(self, key):
        """Deletes the first node found with the matching key (O(n))."""
        current = self.head

        while current:
            if current.data == key:
                # Case 1: Deleting the Head
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None # New head's prev must be None
                    else:
                        self.tail = None      # List became empty
                
                # Case 2: Deleting the Tail
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None     # New tail's next must be None
                
                # Case 3: Deleting a Middle Node
                else:
                    current.prev.next = current.next # Node before bypasses 'current'
                    current.next.prev = current.prev # Node after bypasses 'current'
                
                self.size -= 1
                return
            
            current = current.next
            
        print(f"Key '{key}' not found in list.")
        
    def traverse_backward(self):
        """Allows backward iteration starting from the tail."""
        current = self.tail
        print("Backward Traversal:")
        while current:
            print(current.data)
            current = current.prev
                        
if __name__ == '__main__':
    dll = DoublyLinkedList()

    dll.append(1)    # List: [1]
    dll.append(2)    # List: [1, 2]
    dll.insert_at_beginning(0) # List: [0, 1, 2]
    dll.append(3)    # List: [0, 1, 2, 3]

    print(f"List Size: {len(dll)}") # Output: List Size: 4
    print("Forward Traversal:")
    print([x for x in dll])        # Output: [0, 1, 2, 3]

    dll.delete(2) # Delete a middle node. List: [0, 1, 3]
    dll.delete(0) # Delete the head. List: [1, 3]
    #dll.delete(3) # Delete the tail. List: [1]

    print("\nAfter Deletions:")
    dll.traverse_backward()
    # Output:
    # Backward Traversal:
    # 1
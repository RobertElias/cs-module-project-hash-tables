class LinkedList:
    def __init__(self, HashTableEntry=None):
        self.head = HashTableEntry
        self.tail = HashTableEntry
    
    def __repr__(self):
        return f'{repr(self.head)}'
        
    # this will insert node to tail
    def add_to_tail(self, HashTableEntry):
        new_entry = HashTableEntry
        if self.head is None:
            self.head = new_entry
            self.tail = new_entry
        else:
            self.tail.next = new_entry
            self.tail = new_entry

    def contains(self, key):
        current = self.head
        while current is not None:
            if current.key == key:
                return current.value
            else:
                current = current.next
        return False

    def remove(self, key):
        # item the head and then remove the node

        if self.head.key == key:
            # now matches the memory address on self.head
            victum = self.head
            # head pointer is now pointing to the memory address at head.next (head is now one over)
            self.head = self.head.next
            #  for the previous head is still pointing to
            victum.next = None
        # if it isn't there we check to see if there is a none
        # if there is a none then we return False
        else:
            # else we walk through the array one my array one by one
            # till it is it is none
            current = self.head
            prev = None
            while current.next is not None:
                if current.key == key:
                    prev.next = current.next
                    current.next = None
                    return current.value
                prev = current
                current = current.next
            return False
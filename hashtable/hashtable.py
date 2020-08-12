# from linkedlist import LinkedList
class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
    def __repr__(self):
        return f'{repr(self.key)}'


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8
##################
class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity = MIN_CAPACITY):
        # Your code here
        self.capacity = capacity
        if self.capacity < MIN_CAPACITY:
            self.capacity = MIN_CAPACITY
        self.table = [None for _ in range(capacity)]
        self.count = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.table)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.count/len(self.table)

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        cur = self.table[index]

        while cur is not None and cur.key != key:
            cur = cur.next

        if cur is not None:
            cur.value = value
        
        else: 
            new_entry = HashTableEntry(key, value)
            new_entry.next = self.table[index]
            self.table[index] = new_entry

        # slot, entry = self.table[self.hash_index(
        #     key)], HashTableEntry(key, value)
        # self.count += 1
        # if slot is None:
        #     self.table[self.hash_index(
        #         key)] = LinkedList(entry)
        # else:
        #     slot.insert(entry)
        # print({slot}, self.table)
        self.count += 1
        if self.get_load_factor() > 0.7:
            # print(
                # f"{key} LF: {self.get_load_factor()}")
            self.resize(self.capacity*2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here

        index = self.hash_index(key)
        cur = self.table[index]
        last_entry = None

        while cur is not None and cur.key != key:
            last_entry = cur
            cur = last_entry.next 
        
        if cur is None:
            print('key not found')
        else:
            if last_entry is None:
                self.table[index] = cur.next

        self.count -= 1
        # if slot and slot.contains(key) is not False:
        #     print(self.table)
        #     self.count -= 1
        #     slot.remove(key)
        # else:
        #     return False

        # if self.get_load_factor() < 0.2:
        #     # print(f"{key} LF: {self.get_load_factor()}")
        #     self.resize(int(self.capacity/2))

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here

        index = self.hash_index(key)
        cur = self.table[index]

        while cur is not None:

            if (cur.key == key):
                return cur.value
            cur = cur.next

        # slot = self.table[self.hash_index(key)]
        # if slot and slot.contains(key) is not False:
        #     return slot.value
        # return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        # index = self.hash_index(key)
        # cur = self.table[index]
        if new_capacity < MIN_CAPACITY:
            new_capacity = MIN_CAPACITY
        
        old_table = self.table

        self.capacity = new_capacity
        self.table = [None] * self.capacity
        
        for item in old_table:
            if item is not None:
                cur = item
                while cur is not None:
                    self.put(cur.key, cur.value)
                    cur = cur.next



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    # for i in range(1, 13):
    #     print(i, ht.get(f"line_{i}"))
    print(ht.table)
    # # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")
    print(ht.table)
    # Test if data intact after resizing
    for i in range(1, 13):
        print(i, ht.get(f"line_{i}"))
    # print(ht.get("line_9"))

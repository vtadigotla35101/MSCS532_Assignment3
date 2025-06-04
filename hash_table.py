class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # Initialize an array of empty lists

    def hash_function(self, key):
        return hash(key) % self.size  # Example simple hash function

    def insert(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:  # Check if key already exists
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])  # Add new key-value pair

    def search(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None  # Key not found

    def delete(self, key):
        index = self.hash_function(key)
        self.table[index] = [pair for pair in self.table[index] if pair[0] != key]  # Remove key

    def display(self):
        for i, chain in enumerate(self.table):
            print(f"Index {i}: {chain}")


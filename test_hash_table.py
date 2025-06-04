import unittest
# import sys
# # Redirect output to a file
# sys.stdout = open("test_HashTableResults.log", "w")

from hash_table import HashTable  # Ensure the correct file name

class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.ht = HashTable(size=5)

    def test_insert_and_search(self):
        self.ht.insert("apple", 10)
        self.assertEqual(self.ht.search("apple"), 10)

    def test_search_nonexistent_key(self):
        self.assertIsNone(self.ht.search("orange"))

    def test_update_existing_key(self):
        self.ht.insert("banana", 20)
        self.ht.insert("banana", 25)  # Update value
        self.assertEqual(self.ht.search("banana"), 25)

    def test_delete(self):
        self.ht.insert("grape", 30)
        self.ht.delete("grape")
        self.assertIsNone(self.ht.search("grape"))

if __name__ == "__main__":
    #unittest.main()
    #sys.stdout.close()
    with open("test_HashTableResults.log", "w") as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        unittest.main(testRunner=runner, exit=False)

import random
class RandomizedSet:
  """
  Implement the RandomizedSet class:

  RandomizedSet() Initializes the RandomizedSet object.
  bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
  bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
  int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
  
  You must implement the functions of the class such that each function works in average O(1) time complexity.
  """
    # Define both a dictionary and a list. 
    # the dictionary stores the index of the elements appended in the list
    # with the key being the value 
    # len, pop, append all take O(1) time 
    def __init__(self):
        self.hashmap = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            self.arr.append(val)
            self.hashmap[val] = len(self.arr)-1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            # get the index of the element to be removed
            idx = self.hashmap[val]
            # replace the element with the end value
            self.arr[idx] = self.arr[-1]
            # store the new index of the end value
            self.hashmap[self.arr[-1]] = idx
            # remove the last value from list
            self.arr.pop()
            # remove val from dict
            self.hashmap.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        i = random.randint(0, len(self.arr)-1)
        return self.arr[i]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

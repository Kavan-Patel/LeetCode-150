# 380. Insert Delete GetRandom O(1)

# https://leetcode.com/problems/insert-delete-getrandom-o1/description/?envType=study-plan-v2&envId=top-interview-150

class RandomizedSet:

    def __init__(self):
        # First we initialize Hashmap and the list
        self.set_map = {}
        self.set = []

    def insert(self, val: int) -> bool:
        # Here we checked in the map if value is not there we insert and return True
        if val not in self.set_map:
            # First we update map with value and index (Here len of list)
            self.set_map[val] = len(self.set)
            # now insert value in the list
            self.set.append(val)
            return True
        else:
            return False
        
    def remove(self, val: int) -> bool:
        # First we check if value is present in hashmap then we remove it and return True
        if val in self.set_map:
            # First we find last value and index of value
            val_index = self.set_map[val]
            last_value = self.set[-1]

            # now We're replacing value with the last value 
            self.set[val_index] = last_value

            # update the map for moving the last value to current value index
            self.set_map[last_value] = val_index

            # Simply pop the last value
            self.set.pop()

            # delete the popped value from the map
            del self.set_map[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        # here we use pythong random.choice method to get the random number from the list
        return random.choice(self.set)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
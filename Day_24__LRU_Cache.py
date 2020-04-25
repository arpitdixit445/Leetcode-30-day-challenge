'''
Problem Statement ->
        Design and implement a data structure for Least Recently Used (LRU) 
        cache. It should support the following operations: get and put.

        get(key) - Get the value (will always be positive) of the key if the 
        key exists in the cache, otherwise return -1.
        put(key, value) - Set or insert the value if the key is not already 
        present. When the cache reached its capacity, it should invalidate 
        the least recently used item before inserting a new item.

        The cache is initialized with a positive capacity.
'''

#Solution Using Hasmaps and queues: Time O(1), Space O(n)


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.count = {}
        self.queue = []

        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.queue.append(key)
            self.count[key] += 1
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.cache) < self.capacity:
            if key in self.cache:
                self.count[key] += 1
            else:
                self.count[key] = 1
            self.cache[key] = value
            self.queue.append(key)
        else:
            if key in self.cache:
                self.cache[key] = value
                self.queue.append(key)
                self.count[key] += 1
            else:
                x = 0
                while True:
                    x = self.queue.pop(0)
                    if self.count[x] == 1:
                        del self.count[x]
                        break
                    self.count[x]-=1
                del self.cache[x]
                self.queue.append(key)
                self.cache[key] = value
                self.count[key] = 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

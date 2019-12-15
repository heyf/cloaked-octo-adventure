#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key = list()
        self.storage = dict()
        
    def get(self, key: int) -> int:
        for idx, k in enumerate(self.key):
            if k == key:
                break
        else:
            return -1
        self.key.pop(idx)
        self.key.append(key)
        return self.storage.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if len(self.storage) >= self.capacity:
            del_key = self.key.pop(0)
            del(self.storage[del_key])
        if self.get(key) is -1:
            self.key.append(key)
        self.storage[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
null = None
# WA1
# action = ["LRUCache","put","put","put","put","get","get"]
# inputs = [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]
# ans = [null,null,null,null,null,-1,3]
# WA2
action = ["LRUCache","get","put","get","put","put","get","get"]
inputs = [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
ans = [null,-1,null,-1,null,null,2,6]
ret = []
for a, i in zip(action, inputs):
    if a == "LRUCache":
        cache = LRUCache(i[0])
        ret.append(None)
    if a == "put":
        ret.append(cache.put(i[0], i[1]))
    if a == "get":
        ret.append(cache.get(i[0]))
print(ret)
from functools import reduce
print(reduce(lambda x, y: x and y,[ a == b for a, b in zip(ans, ret)]))
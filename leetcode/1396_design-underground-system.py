# 1396. Design Underground System - LeetCode
# https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.time_sheet = dict() # key=(startStation, endStation), value=(count, total)
        self.checkin_cache = dict() # key=id

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if self.checkin_cache.get(id):
            return
        self.checkin_cache.update({id: (stationName, t)})

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        endStation = stationName
        if self.checkin_cache.get(id):
            startStation, startTime = self.checkin_cache.get(id)
            del(self.checkin_cache[id])
            count, total = 0, 0
            if self.time_sheet.get((startStation, endStation)):
                count, total = self.time_sheet.get((startStation, endStation))
            self.time_sheet.update({(startStation, endStation): (count+1, total+t-startTime)})
        return

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        count, total = self.time_sheet.get((startStation, endStation))
        return total / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

obj = UndergroundSystem()
obj.checkIn(1, "A", 1)
obj.checkIn(2, "A", 1)
obj.checkOut(2, "B", 4)
obj.checkOut(1, "B", 3)
print(obj.getAverageTime("A", "B"))

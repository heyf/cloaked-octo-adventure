# 1418. Display Table of Food Orders in a Restaurant - LeetCode
# https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/

from typing import List

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        order_set = set()
        tables = {} # id: { "order": count }
        ret = []
        for order in orders:
            _, number, name = order
            if name not in order_set:
                order_set.add(name)
            if not tables.get(number, False):
                tables[number] = dict()
            if not tables[number].get(name, False):
                tables[number][name] = 0
            tables[number][name] += 1
        order_list = sorted(list(order_set))
        title = ["Table"] + list(order_list)
        ret.append(title)

        number_list = sorted([int(number) for number in tables])
        for number in number_list:
            number = str(number)
            table = tables[number]
            table_order = [number] + [ str(table.get(name, 0)) for name in order_list ]
            ret.append(table_order)
        return ret

orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
sl = Solution()
ret = sl.displayTable(orders)
print(ret)

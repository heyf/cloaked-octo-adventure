#
# @lc app=leetcode id=218 lang=python3
#
# [218] The Skyline Problem
#
from typing import List

# @lc code=start
from collections import namedtuple

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ret = []
        Building = namedtuple("Building", ["left", "right", "height"])
        active_list = []
        keypoint_list = []
        for li, ri, _ in buildings:
            keypoint_list += [ li, ri ]
        keypoint_list = sorted(keypoint_list)
        for keypoint in keypoint_list:
            if buildings[0][0] >= keypoint:
                building = buildings.pop(0)
                active_list.append(Building(left=building[0], right=building[1], height=building[2]))
            active_building = None

            if ret :
                pass
            else:
                if active_building:
                    ret.append([active_building.left, active_building.right])
            


        return ret
        
# @lc code=end
s = Solution()
buildings = [ [2,9,10], [3,7,15], [5,12,12], [15,20,10], [19,24,8] ]
ret = s.getSkyline(buildings)
print(ret)
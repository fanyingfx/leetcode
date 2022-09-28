# @algorithm @lc id=1287 lang=python3 
# @title distance-between-bus-stops

from typing import List, Optional
from cn.Python3.mod.preImport import *
# @test([1,2,3,4],0,1)=1
# @test([1,2,3,4],0,2)=3
# @test([1,2,3,4] ,0,3)=4
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        
        # 0->1 a[0]
        # 0->2 a[0]+a[1]
        # 2->3 a[2]+a[3]
        total=sum(distance)

        if start > destination:
            start,destination=destination,start
        
        
        return min(sum(distance[start:destination]),total-sum(distance[start:destination]))
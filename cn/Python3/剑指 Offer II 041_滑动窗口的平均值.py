# @algorithm @lc id=1000292 lang=python3 
# @title qIsx9U

from collections import deque
class MovingAverage:
    def __init__(self,size) -> None:
        self.windows=deque(maxlen=size)
    
    def next(self,val:int) -> float:
        self.windows.append(val)
        return sum(self.windows)/len(self.windows)

        
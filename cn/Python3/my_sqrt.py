def sqrt(v:int,e:float):
    left = 0
    right=(v+3)//2
    while left<right:
        mid = (left+right)/2
        if v>((v+mid*mid-e*e)/(2*mid))**2:
            return mid
        if mid*mid > v:
            right=mid - e
        else:
            left = mid+e

print(sqrt(2,0.001))
print(sqrt(4,0.001))
print(sqrt(5,0.001))
print(sqrt(6,0.001))

import math
print(math.sqrt(3)-sqrt(3,0.001))
#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x ==-2**31:return 0
        l = []

        max_sub  = (2**31-1) % (10**9)
        pos = 1
        if x < 0:
            pos = -1
            x = -x
            max_sub+=1

        
        while x != 0:
            l.append(x%10)
            x = x//10
        res = 0
        l.reverse()
        for i in range(len(l)):
            if i ==9:
                print(l[i])
                print(res,max_sub)
                if l[i] > 2:
                    return 0
                elif l[i] == 2 and res > max_sub:
                    return 0
            
            res = res + l[i]*10**i
        return pos*res




sln = Solution()
print(sln.reverse(-2147483412))
        
        

# @lc code=end


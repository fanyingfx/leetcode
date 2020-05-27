#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []

        num_alpha={
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        res = ['']

        for digit in digits:
            new_res = []
            for a in num_alpha[digit]:
               for r in res:
                   new_res.append(r+a)
            res = new_res
        
        return list(res)

sln = Solution()

print(sln.letterCombinations('7'))
# @lc code=end


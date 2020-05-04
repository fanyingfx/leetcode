#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s
        def expand(i):
            curr1 = s[i]
            left = i
            right = i

            def find(center,left,right):
                curr= center
                while True:
                    left -=1
                    right +=1
                    if left < 0 or right > len(s)-1:
                        break
                    if s[left]==s[right]:
                        curr=s[left]+curr+s[right]
                    else:break
                return curr

            curr1=find(curr1,left,right) 

            left,right=i,i
            if s[i+1]==s[i]:
                curr2 = s[i]+s[i+1]
                right += 1
                curr2=find(curr2,left,right)
                
                if len(curr2)>len(curr1):
                    return curr2
            return curr1
            
                
        max_palindrome = s[0]

        for i in range(len(s)-1):
            cu = expand(i)
            if len(cu) > len(max_palindrome):
                max_palindrome=cu
        return max_palindrome

sln=Solution()
print(sln.longestPalindrome('abbba'))





# @lc code=end


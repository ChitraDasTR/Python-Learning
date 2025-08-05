

# 2239. Find Closest Number to Zero

class Solution:

    def findClosestNumber(self, nums: list[int]) -> int:
    
        nums = list(set(nums))
        nums.sort()

        min_diff = 999999999
        closest_num = None

        for num in nums:
            curr_diff = abs(num - 0)

            if curr_diff < min_diff:
                min_diff = curr_diff
                closest_num = num
            
            elif curr_diff == min_diff:
                closest_num = max(closest_num, num)

        return closest_num



# 1768. Merge Strings Alternately

class Solution:

    def mergeAlternately(self, word1: str, word2: str) -> str:
    
        new_word = ''
        for i in range(min(len(word1), len(word2))):
            new_word += word1[i] + word2[i]

        if len(word1) > len(word2):
            new_word += word1[len(word2):]
    
        else:
            new_word += word2[len(word1):]

        return new_word




# 121. Best Time to Buy and Sell Stock

class Solution:
   
    def maxProfit(self, prices: list[int]) -> int:        
   
        min_price = prices[0]
        max_profit = 0
   
        for price in prices:
   
            if price < min_price:
                min_price = price
   
            elif price - min_price > max_profit:
                max_profit = price - min_price
   
        return max_profit



#14. Longest Common Prefix

class Solution:

    def longestCommonPrefix(self, strs: list[str]) -> str:
    
        if not strs:
            return "" 

        prefix = strs[0]

        for s in strs[1:]:
            i = 0
    
            while i < len(prefix) and i < len(s) and prefix[i] == s[i]:
                i += 1
           
            prefix = prefix[:i]

        return prefix




# 13. Roman to Integer

class Solution:
    
    def romanToInt(self, s: str) -> int:
    
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        summ = 0
        n = len(s)
        i = 0
    
        while i < n:
    
            if i < n - 1 and d[s[i]] < d[s[i + 1]]:
                summ += d[s[i + 1]] - d[s[i]]
                i += 2
    
            else:
                summ += d[s[i]]
                i += 1
    
        return summ


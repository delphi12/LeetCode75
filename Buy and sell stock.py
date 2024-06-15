#You are given an array prices where prices[i] is the price of a given stock on the ith day.

#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0

def maxProfit(nums):
    l,r = 0,1
    n = len(nums)
    max_Profit = 0

    for r in range(n):
        if nums[l]<nums[r]:
            p = nums[r] - nums[l]
            max_Profit = max(p, max_Profit)
        else:
            l=r
        r+=1
    print("Maximum Profit ", max_Profit)

nums = [7,1,5,3,6,4] #output:5
#nums = [7,6,4,3,1] #output:0
maxProfit(nums)


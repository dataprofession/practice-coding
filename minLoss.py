# Minimum Loss Problem
# Source: HackerRank - https://www.hackerrank.com/challenges/minimum-loss/problem
# Solution:
# The mininumLoss function sorts prices with their original indices and checks pairs to find the minimum loss \
# by ensuring that the selling index is greater than the buying index. 
# It focuses on comparing prices from the sorted list while keeping track of their original positions.

import sys
def minimumLoss(price):
    
    loss = sys.maxsize
        
    price_with_indices =[(price[i],i) for i in range(len(price))]
    
    price_with_indices.sort()
    
    for i in range(1, len(price)):
        current_price, current_index = price_with_indices[i]
        last_price, last_index = price_with_indices[i-1]
        
        if current_index < last_index:
            loss = min(loss,current_price - last_price)
            
    return loss

import unittest

class TestGetMoneySpent(unittest.TestCase):
    
    def test_case_1(self):
        price = [20,7,8,2,5]
        result = minimumLoss(price)
        self.assertEqual(result, 2)

    def test_case_2(self):
        price = [2,3,4,1]
        result = minimumLoss(price)
        self.assertEqual(result, 1)

if __name__ == "__main__":
    unittest.main()
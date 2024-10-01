# Electronics Shop Problem
# Source: HackerRank - https://www.hackerrank.com/challenges/electronics-shop/problem
# Solution uses two loops to find the maximum money spent.

import unittest
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    cost = -1
    k = 0
    d = 0
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            if keyboards[i] + drives[j] <= b:
                cost = max(cost, keyboards[i]+drives[j])
                k = i
                d = j
    return cost

class TestGetMoneySpent(unittest.TestCase):
    
    def test_case_1(self):
        keyboards = [40, 50, 60]
        drives = [5, 8, 12]
        budget = 60
        result = getMoneySpent(keyboards, drives, budget)
        self.assertEqual(result, 58)

    def test_case_2(self):
        keyboards = [40, 50, 60]
        drives = [5, 8, 12]
        budget = 60
        result = getMoneySpent(keyboards, drives, budget)
        self.assertEqual(result, 58)

    def test_case_3(self):
        keyboards = [40]
        drives = [5]
        budget = 50
        result = getMoneySpent(keyboards, drives, budget)
        self.assertEqual(result, 45)

    def test_case_no_combination(self):
        keyboards = [70, 80]
        drives = [10, 20]
        budget = 50
        result = getMoneySpent(keyboards, drives, budget)
        self.assertEqual(result, -1)

if __name__ == "__main__":
    unittest.main()
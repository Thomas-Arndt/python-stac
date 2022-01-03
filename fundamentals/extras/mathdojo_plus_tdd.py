import unittest

class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for number in nums:
            self.result += number
        return self.result

    def subtract(self, num, *nums):
        self.result += num
        for number in nums:
            self.result -= number
        return self.result


class MathDojoTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(self.md.add(1,2,3,4,5), 15)
    
    def test_subtract(self):
        self.assertEqual(self.md.subtract(5,3,2,1), -1)
    
    def test_add_negatives(self):
        self.assertEqual(self.md.add(1,2,-3,4,-5), -1)
    
    def test_subtract_negatives(self):
        self.assertEqual(self.md.subtract(1,2,-3,4,-5), 3)

    def setUp(self):
        self.md=MathDojo()

if __name__=="__main__":
    unittest.main()
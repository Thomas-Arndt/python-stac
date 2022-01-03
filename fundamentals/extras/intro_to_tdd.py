import unittest
import math

def reverse_list(list):
    if len(list)<2:
        return list
    left=0
    right=len(list)-1
    while left<right:
        temp=list[left]
        list[left]=list[right]
        list[right]=temp
        left+=1
        right-=1
    return list

def is_palindrome(string):
    if len(string)<2:
        return True
    left=0
    right=len(string)-1
    while left<right:
        if string[left]!=string[right]:
            return False
        left+=1
        right-=1
    return True

def coins(change):
    coins=[]
    coin_dict={
        "quarter": 25,
        "dime": 10,
        "nickel": 5,
        "penny": 1
    }
    for coin in coin_dict:
        
        if change/coin_dict[coin]>=1:
            coins.append(math.floor(change/coin_dict[coin]))
        else:
            coins.append(0)
        change-=coins[-1]*coin_dict[coin]
    return coins

def factorial(num, i=1):
    if num<0:
        return False
    if num==0:
        return 0
    if i==num:
        return i
    return factorial(num, i+1)*i

def fibonacci(num):
    if num<0:
        return False
    if num<2:
        return num
    return fibonacci(num-1)+fibonacci(num-2)

class reverse_list_tests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse_list([]), [])

    def test_single_value(self):
        self.assertEqual(reverse_list([1]), [1])
    
    def test_reverse(self):
        self.assertEqual(reverse_list([1,2,3,4,5]), [5,4,3,2,1])

class is_palindrome_tests(unittest.TestCase):
    def test_empty(self):
        self.assertTrue(is_palindrome(''))
    
    def test_one_character(self):
        self.assertTrue(is_palindrome('a'))

    def test_palindrome(self):
        self.assertTrue(is_palindrome('racecar'))
    
    def test_non_palindrome(self):
        self.assertFalse(is_palindrome('hello'))
    
    def test_blank_space_palindrome(self):
        self.assertTrue(is_palindrome("hello olleh"))
    
    def test_blank_space_non_palindrome(self):
        self.assertFalse(is_palindrome('race car'))

class coins_tests(unittest.TestCase):
    def test_zero_change(self):
        self.assertEqual(coins(0), [0,0,0,0])
    
    def test_pennies(self):
        self.assertEqual(coins(3), [0,0,0,3])
    
    def test_nickels(self):
        self.assertEqual(coins(5), [0,0,1,0])
    
    def test_dimes(self):
        self.assertEqual(coins(10), [0,1,0,0])
    
    def test_quarters(self):
        self.assertEqual(coins(50), [2,0,0,0])
    
    def test_dimes_and_pennies(self):
        self.assertEqual(coins(13), [0,1,0,3])
    
    def test_all_coins(self):
        self.assertEqual(coins(69), [2,1,1,4])

class factoril_tests(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(factorial(0), 0)
    
    def test_negative(self):
        self.assertFalse(factorial(-1))

    def test_five(self):
        self.assertEqual(factorial(5), 120)
    
    def test_ten(self):
        self.assertEqual(factorial(10), 3628800)
    
    def test_three(self):
        self.assertEqual(factorial(3), 6)

class fibonacci_tests(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(fibonacci(0), 0)
    
    def test_one(self):
        self.assertEqual(fibonacci(1), 1)
    
    def test_two(self):
        self.assertEqual(fibonacci(2), 1)
    
    def test_five(self):
        self.assertEqual(fibonacci(5), 5)
    
    def test_nine(self):
        self.assertEqual(fibonacci(9), 34)
    
    def test_negative(self):
        self.assertFalse(fibonacci(-1))


if __name__=="__main__":
    unittest.main()
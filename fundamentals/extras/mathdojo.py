class MathDojo:
    def __init__(self):
    	self.result = 0

    def add(self, num, *nums):
        self.result += num
        for number in nums:
            self.result += number
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for number in nums:
            self.result -= number
        return self

# create an instance:
md = MathDojo()
# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5
# run each of the methods a few more times and check the result!
y = md.add(4).add(3,7).add(1,4,9).result
print(y)

z = md.subtract(10).subtract(2,3).subtract(1,2).result
print(z)

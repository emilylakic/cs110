import random
def computeSum(nums):
	accum = 0
	for i in nums:
		accum += i
	return accum

def computeAverage(nums):
	length = len(nums) #used to have .len here just check
	a = computeSum(nums)
	avg = a/length
	return avg

def findMiddleValue(nums):
	avg = computeAverage(nums)
	result = abs(avg - nums[0])
	middle = 0
	for i in nums:
		difference = abs(avg-i)
		if (result>difference):
			result = difference
			middle = i
	return middle

def createRandomInts(nums):
	myList = []
	for i in range(nums):
		myList2 = myList.append(random.randint(1,100))
	return myList

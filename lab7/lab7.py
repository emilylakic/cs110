import listoperations
import string
user = input("Enter a word: ")
useThese = string.ascii_letters
myList = []
def countAll():
    #for i in range(0, len(user)):
    for i in range(0,1):
        for x in range(0,26):
            myList.append(user.count(useThese[x])+user.count(useThese[x+26]))
    print(myList)

def main():
	myList = listoperations.createRandomInts(10)
	print(myList)
	print(listoperations.computeSum(myList))
	print(listoperations.computeAverage(myList))
	print(listoperations.findMiddleValue(myList))
	countAll()
main()

#logic behind this
#put all of this in a for loop for the entire alphabet, not just one letter
#alpha = string.ascii_letters() #alphabet
#>>count = 0
#>>#lettersList = []
#>>for every letter in range(a to z):
#>>	if the letter in the user inputted is the same as the letter in the alphabet:
#>		count +=1
#>>print(count)
#if the letter (i) in the user inputted word shows up in the
#alphabet, then count it (count+=1) (start off count = 0)

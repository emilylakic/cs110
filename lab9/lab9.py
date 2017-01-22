def countAll(word):
	mydict = {}
	letters = [chr(i+97) for i in range(26)]
	for i in range(len(letters)):
		small = word.count(letters[i])
		high = word.count(letters[i].upper())
		if(small+high>0):
			mydict[letters[i]] = small+high
	return mydict
def main():
	countString = input("Write a string: ")
	print(countString + ":" + str(countAll(countString)))
main()

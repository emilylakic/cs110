import string
user = input("Enter a word: ")
useThese = string.ascii_letters
myList = []
def countAll():
    for i in range(0,1):
        for x in range(0,26):
            myList.append(user.count(useThese[x])+user.count(useThese[x+26]))
    print(myList)
def main():
    countAll()
main()

import string
user = input("Enter a word: ")
useThese = string.ascii_letters
my_dict = {}
def countAll():
    for i in range(0,1):
        for x in range(0,26):
            my_dict[x] = user.count(useThese[x])
            my_dict[x] = user.count(useThese[x+26])
    print(my_dict)
def main():
    countAll()
main()

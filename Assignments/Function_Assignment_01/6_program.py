'''
6. Python program that defines a parent function with two nested functions
(myIndex and myPalindrome). The program prompts the user to choose between
these two functions and then calls the selected function based on the user's
input.
Choice = 1
listData = [1, 2, 3, 4, 5, 6]
searchEle = 2
Output: 1

Choice = 2
Num = 141
Output: True
'''

def Parent():

    def myIndex(Data,No):
        count = 0
        for i in Data:
            if i == No:
                count+=1

        print(count)

    def myPalidrome(num):

        Pali = 0
        while 0<num:
            rem = num%10
            pali = pali*20+rem
            num = num//10
        if pali == num:
            print("True")

listData = [1,2,3,4,5,6]

user = int(input("Enter user Choice No. : "))

if user == 1:

    serarNo = 2
    Parent()
    ret = myIndex(listData,seraNo)

if user == 2:

    Num = 141
    ret = parent()
    ret(Num)


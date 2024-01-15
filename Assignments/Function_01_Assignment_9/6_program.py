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

def Parent(Data, searNo, Num, Choise):

    def myIndex(Data,searNo):
        count = 0
        for i in Data:
            if i == searNo:
                count+=1

        print(count) 

    def myPalidrome(num):

        num1 = num
        Pali = 0
        while 0<num:
            rem = num%10
            Pali = Pali*10+rem
            num = num//10
        if Pali == num1:
            print("True")
        else:
            print("False")

    if Choise == 1:
        myIndex(Data, searNo)

    if Choise == 2:
        myPalidrome(Num)
    
listData = [1,2,3,4,5,6]
searNo = 2

user = int(input("Enter user Choice No. : "))
Num = 1134311
Parent(listData,searNo, Num, user)


'''
if user == 1:

    serarNo = 2
    Parent()
    ret = myIndex(listData,seraNo)

if user == 2:

    Num = 141
    retObj = Parent()
    retObj(Num)
    
'''


"""
Program 5:
WAP to print the number divisible by 7 but not divisible by 3 between 1 to 100
Input :
Enter start of range - 1
Enter end of range - 100
Output :
7
14
28
35
49
56
70
77
91
98

"""


start = int(input("Enter start of range : "))
end = int(input("Enter end of range : "))


for i in range(start,end):

    if (i % 7 == 0) and (i % 3 != 0):
        print(i,end = "   ")



#O/p 7   14   28   35   49   56   70   77   91   98 


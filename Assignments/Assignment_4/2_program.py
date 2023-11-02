"""
Program 2:
Write a Program to print all Even numbers from a given range.
Input :
Start = 10;
End = 20;
Output:
10 12 14 16 18

"""


start = int(input("Enter value of start : "))
end = int(input("Enter value of end : "))

for i in range(start,end):
    if (i % 2 == 0):
        print(i,end = " ")





# O/p 10 12 14 16 18


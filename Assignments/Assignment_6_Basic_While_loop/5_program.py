"""
5. WAP to print the first 10 negative numbers which is less than the
given number.
Input:
-5
Output:
first 10 negative numbers less than -5 are
-6 -7 -8 -9 -10 -11 -12 -13 -14 -15
"""

less_num = int(input("Enter Value (less then) of num : "))
first_no = int(input("Enter value of first_no : "))
i = less_num - 1
limit = less_num-first_no
print("first 10 negative number less than {} are".format(less_num))


while i >= limit:

    print(i,end = " ")
    i-=1
    
   

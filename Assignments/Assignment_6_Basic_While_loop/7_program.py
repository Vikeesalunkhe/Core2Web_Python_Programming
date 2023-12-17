"""
7. WAP to find the nth odd number.
Input: 3
Output: od number at position 3 is 5
"""

num = int(input("Enter Value of nth no. : "))
i = 1
count = 0

while i <= num+num:
    
    if i % 2 == 1:
        count+=1
        if count == num:
            print(f"odd number at position {num} is {i}")
    i+=1

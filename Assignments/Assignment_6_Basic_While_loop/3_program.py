"""3. WAP to find the 7th odd number (start from 1)
Output:
7th odd number is 13
"""

num = int(input("Enter value of num (position of odd no.) : "))

count = 0 
i = 1

while True:
    if i % 2 == 1:
        count+=1
        if count == num:
            print(num,"th odd number is",i)
            break

    i+=1

'''
2. Write a program to check whether the number is a Prime
number or not. (2332)
Input:2332
Output:2332 is not a prime number
'''

def PrimeNo(num):
    
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count+=1


    return count

num = int(input("Enter value of prime no : "))
ret = PrimeNo(num)
if ret == 2:
    print(f"{num} is prime number")

else:
    print(f"{num} is not a prime number")


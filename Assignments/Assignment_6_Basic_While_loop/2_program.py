"""
2. WAP to calculate the sum of the first 10 even numbers.
Output:
Sum of first 10 even numbers is 110
"""
num = int(input("Enter value of first sum off no.  : "))

even_sum = 0
i = 1

while i <= num+num:
    
    if i % 2 == 0:
        even_sum+=i

    i+=1

print("sum of first {} even number is {}".format(num,even_sum))

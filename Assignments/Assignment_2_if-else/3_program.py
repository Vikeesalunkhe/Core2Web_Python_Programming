"""

3. Take two numbers from users and print the sum of those numbers if the sum is even.
Input1: num1 = 10
Input2: num2 = 20
Output: 30 is Even
Input1: num1 = 10
Input2: num2 = 15
Output:No Output

"""

num1 = int(input("Enter value of num1 : "))
num2 = int(input("Enter value of num2 : "))

_sum = num1 + num2

if (_sum % 2 == 0):
    print("{} is Even".format(_sum))

else:
    print("No Output")

num1 = num = int(input("Enyter value of num : "))
rev = 0

while num>0:

    rem = num%10
    rev = rev*10+rem
    num = num//10

print(f"Input no. is {num1} and reverse is {rev}")

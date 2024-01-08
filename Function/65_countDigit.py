'''
4. Write a program to count the digits of the given number.
Input:942111423
Output: 9
'''

def DigiCount(num):
    
    count = 0 
    while num>0:
        num = num//10
        count +=1

    return count

x = int(input("Enter value of num : "))
ret = DigiCount(x)
print("Total no. of digit is :",ret)
        





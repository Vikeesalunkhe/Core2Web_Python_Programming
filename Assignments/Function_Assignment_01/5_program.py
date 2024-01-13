'''
5. Write the parent function that includes the nested functions digitCount,
evenDigitCount, and oddDigitCount. provide a number to th functions Then, call
all functions and fill in the return value in the list.
Input:
Num = 12345
Output: [5, 2, 3]
'''

def Parent(num):

    def DigiCount(num):
        count = 0
        while 0 < num:
            num= num //10
            count+=1

        OutPut.append(count)
    DigiCount(num)

    def evenDigit(num):
        count = 0
        while 0<num:
            rem = num%10
            if rem % 2 == 0:
                count+=1
            num = num//10
        OutPut.append(count)
    evenDigit(num)

    def oddDigit(num):
        count = 0
        while 0<num:
            rem = num%10
            if rem % 2 == 1:
                count+=1
            num = num//10
        OutPut.append(count)
    oddDigit(num)


Num = int(input("Enter value of num : "))
OutPut = []
Parent(Num)
print(OutPut)



"""
5. Write the parent function that includes the nested functions digitCount,
evenDigitCount, and oddDigitCount. Prompt the user to choose the desired
function and provide a list of elements. Then, invoke the selected function based
on the user's choice and the input list
"""

def Count(my_list):

    def DigitCount(my_list):
        digicount = 0
        for i in my_list:
           digicount+=1
        print("Digit cont is : ",digicount)
        return EvenCount

    def EvenCount(my_list):
        evencount = 0
        for i in my_list:
            if i % 2 == 0:
               evencount+=1
        print("Even count is : ",evencount)
        return OddCount
    
    def OddCount(my_list):
        oddcount = 0
        for i in my_list:
            if i % 2 == 1:
                oddcount+=1
        print("Odd count is : ",oddcount)

    return DigitCount
    

my_list = [1,2,3,4,5,6,7,8,9,10]
Digiret = Count(my_list)
Evenret = Digiret(my_list)
Oddret = Evenret(my_list)
Oddret(my_list)


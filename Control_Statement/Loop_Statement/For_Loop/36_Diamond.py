'''
        *
      * * *
    * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''

def Pattern(num):

    for i in range(num):
        for j in range(num-i+1):
            print(" ", end= " ")

        for j in range(2*i+1):
            print("*", end =" ")

        for j in range(num-i-1):
            print(" ", end = " ")
        

        print()
    num-=1
    for i in range(num):
        for j in range(i):
            print(" ",end = " ")

        for j in range(2*num -(2*i+1)):
            print("*", end = " ")

        for j in range(i):
            print(" ", end = " ")

        print()

      
num = int(input("Enter value of num : "))
Pattern(num)

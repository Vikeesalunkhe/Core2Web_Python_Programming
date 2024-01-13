'''
     *
    ***
   *****
  *******
'''

def Diamond(num):

    for i in range(num):
        for j in range(num-i-1):
            print(" ", end = " ")

        for j in range(2*i+1):
            print("*", end= " ")

        for j in range(num-i-1):
            print(" ",end = " ")

        print()


num = int(input("Enter value of num : "))
Diamond(num)

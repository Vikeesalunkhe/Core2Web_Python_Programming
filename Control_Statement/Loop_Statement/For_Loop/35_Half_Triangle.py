'''
* * * *
  * * *
    * *
      *
'''

def pattern(num):

    for i in range(num):
        for j in range(i):
            print(" ",end= " ")

        for j in range(num-i):
            print("*", end = " ")

        print()

num = int(input("Enter value of num : "))
pattern(num)

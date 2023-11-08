"""

1 0 1 0 1
1 0 1 0
1 0 1
1 0
1

"""

def pattern():

    def pattern1():
        i = 0
        while(i < 5):
            j = 0
            while(j < 5-i):
                if (j%2==0):
                    print("1",end = " ")

                else:
                    print("0",end = " ")

                j+=1

            print()
            i+=1
    pattern1()
pattern()


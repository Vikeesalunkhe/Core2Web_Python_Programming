def pattern(x,y):
    
    i = 1
    while i<= x:
        j = 1
        while j<= y:
            print("*",end = " ")
            j += 1

        print()
        i += 1

row = int(input("enter va;ue of row : "))
column = int(input("Enyter value of column : "))
ret = pattern(row, column)


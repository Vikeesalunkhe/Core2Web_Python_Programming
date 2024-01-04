"""
Program7 : Row = 5
E D C B A
A B C D E
E D C B A
A B C D E
E D C B A
"""
rows = int(input("Enter Value of rows number : "))
A = 65
E = 69
for i in range(1,rows+1):
    for j in range(1,rows+1):

        if i % 2 == 1:
            print(chr(E), end = " ")
            E-=1

        else:
            print(chr(A), end = " ")
            A+=1

    print()
    A = 65
    E = 69



"""
2.

5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
"""
num = int(input("Enter Value of Row number : "))
for i in range(1,num+1):
    data = num
    for j in range(i):
        print(data, end = " ")
        data-=1

    print()

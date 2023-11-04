"""
Program9:
Row = 3
1 3 5
3 5 7
5 7 9

"""

row = int(input("Enter the row value : "))

for i in range(1,6,2):
    num = i
    
    for j in range(row):
        print(num,end = " ")
        num += 2
    
    print()
    


#print = 5 * 15 * 25 * 35 * 45 *

x = 50

for i in range(5, x+1, 5):

    if (i % 2 == 0):

        print("*", end = " ")         #10 20 30 40 50

    else:

        print(i, end = " ")

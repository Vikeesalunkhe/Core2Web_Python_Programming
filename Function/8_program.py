#print star using def function

def starprint(x):

    for i in range(x):
        for j in range(x):
            print("*",end = " ")

        print()


star_range = int(input("Enter value of range : "))
starprint(star_range)

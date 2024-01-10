import array

my_arr = array.array('i',[111,212,345543,874])
print(my_arr)

palindromNo = set() 

for i in my_arr:

    num = num1 = i
    j = 0
    palin = 0
    while (num>0):

        rem = num % 10
        palin = palin*10 + rem
        num = num//10

    if num1 == palin:

        print(f"{num1} is Palindrom")
        palindromNo.add(num1)


    else:
        print(f"{num1} is not a Palindrom")

print("This is Palindrom No. set : ",palindromNo)



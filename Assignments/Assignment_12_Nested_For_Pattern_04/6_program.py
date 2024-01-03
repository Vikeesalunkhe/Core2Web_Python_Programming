"""
Program6 : Row = 4

$ = $ =
= $ = $
$ = $ =
= $ = =
"""
rows = int(input("Enter value of rows number : "))
doller = 36
equal = 61
for i in range(1,rows+1):
    if i % 2 == 1:
        for j in range(1,rows+1):
            if j % 2 == 1:
                print(chr(doller), end = " ")

            else:
                print(chr(equal), end = " ")


    else:
        
        for j in range(1,rows+1):
            if j % 2 == 1:
                print(chr(equal), end = " ")

            else:
                print(chr(doller), end = " ")

    print()

print()
"""
OR
"""
print()


doller = 36
equal = 61
for i in range(1,5):
    for j in range(1,5):

        if i % 2 == 1:

            if j % 2 == 1:
                print(chr(doller), end = " ")

            else:
                print(chr(equal), end = " ")

        else:

            if j % 2 == 1:
                print(chr(equal), end = " ")

            else:
                print(chr(doller), end = " ")

    print()

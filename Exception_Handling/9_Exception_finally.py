#Exception Handling

def Add(num1, num2):

    try:
        result = num1/num2

    except ZeroDivisionError as e:
        print(f"{e} handling Error")


    else:
        print("Result id : ",result)
    
    finally:
        print("Finally All code is Execute")



try:
    num1 = int(input("Enter Value of num1 : "))
except ValueError:
    print("Value Error Handeld : add proper int no. ")
    num1 = int(input("Enter value of num1 : "))

try:
    num2 = int(input("Enter value of num2 : "))
except ValueError:
    print("Value Error handeld")
    num2 = int(input("Enter value of num2 : "))


Add(num1, num2)


    

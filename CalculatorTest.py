#Program to make a simple calculator for conversions to metric from imperial
#where user only has to input the imperial measurement

#This function adds two imperial numbers and yields a metric answer
def add(x, y):
    return round((x+y)*25.4,3)

#This function subtracts two imperial numbers and yields a metric answer
def subtract(x, y):
    return round((x-y)*25.4,3)

#This function multiples two imperial numbers and yields a metric answer
def multiply(x, y):
    return round((x*y)*25.4,3)

#This function divides two imperial numbers and yields a metric answer
def divide(x, y):
    return round((x/y)*25.4,3)

def main():
    print(".......................................................")
    print("Welcome to the basic inches to millimeters conversion tool")
    print(".......................................................")
    print("Please, Select operation:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    #Take input from the user
    choice = input("Enter option(1/2/3/4):")

    if choice == "1":
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "+",num2,"=", add(num1,num2))
        except ValueError:
            print("You must input a number. Try again...")

    elif choice == "2":
        try:
            num1 = float(input("Enter number to subtract from: "))
            num2 = float(input("Enter number to subtract: "))
            print(num1,"-",num2,"=", subtract(num1,num2))
        except ValueError:
            print("You must input a number. Try again...")

    elif choice == "3":
        try:
            num1 = float(input("Enter number to multiply: "))
            num2 = float(input("Enter number to multiply by: "))
            print(num1,"x",num2,'=',multiply(num1,num2))
        except ValueError:
            print("You must input a number. Try again...")

    elif choice=="4":
        try:
            num1 = float(input("Enter number to divide: "))
            num2 = float(input("Enter number to divide by: "))
            print(num1,"/",num2,"=", divide(num1,num2))
        except ValueError:
            print("You must input a number. Try again...")

    else:
        print("     ----------Invalid input peasant----------")
    print(".......................................................")
    restart=input("Do you wish to start again? \"y\" for yes, anything else to exit: ").lower()
    if restart == "y":
        main()

    else:
        print("Untile we meet again...")
        print(".......................................................")
        print(".......................................................")
        exit()

main()
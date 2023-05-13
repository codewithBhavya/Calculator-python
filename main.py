import math
print("welcome to Advanced Calculator")
print("Type :")
print("1.For Addition")
print("2.For Subtraction")
print("3.For Multiplication")
print("4.For Division")
print("5.To find the square root of a Number")
print("6.To find the square of a number")
print("7.To find the cube of a number")
operation_input = input("please enter the arithmetic operator you want to calculate")
operation = int(operation_input)
#computing all the data
if operation == 1:
    num1_input = input("please enter your first number")
    num1 = int(num1_input)
    num2_input = input("please enter your second number")
    num2 = int(num2_input)
    resultant_add = num1 + num2
    print(resultant_add)
elif operation == 2:
    num1_input = input("please enter your first number")
    num1 = int(num1_input)
    num2_input = input("please enter your second number")
    num2 = int(num2_input)
    resultant_sub = num1 - num2
    print(resultant_sub)
elif operation == 3:
    num1_input = input("please enter your first number")
    num1 = int(num1_input)
    num2_input = input("please enter your second number")
    num2 = int(num2_input)
    resultant_multiply = num1 * num2
    print(resultant_multiply)
elif operation == 4:
    num1_input = input("please enter your first number")
    num1 = int(num1_input)
    num2_input = input("please enter your second number")
    num2 = int(num2_input)
    resultant_div = num1 / num2
    print(resultant_div)
elif operation==5:
    num_sqrt = input("enter the number to be square root")
    num_root = int(num_sqrt)
    num = math.sqrt(num_root)
    print(num)
elif operation==6:
    square_input = input("enter the number to be squared")
    square_number = int(square_input)
    square_final = str(square_number*square_number)
    print("the square of is " + square_final)
elif operation==7:
    cube_input = input("enter the number to be cubed")
    cube_number = int(cube_input)
    cube_final = str(cube_number*cube_number*cube_number)
    print("the square of is " + cube_final)
else:
    print("Invaild")

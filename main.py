import math
print("welcome to Advanced Calculator")


operation_input = input("please enter the arithmetic operator you want to calculate")
operation = int(operation_input)
num1_input = input("please enter your first number")
num1 = int(num1_input)
num2_input = input("please enter your second number")
num2 = int(num2_input)

#computing all the data


if operation == 1:
    resultant_add = num1 + num2
    print(resultant_add)
elif operation == 2:
    resultant_sub = num1 - num2
    print(resultant_sub)
elif operation == 3:
    resultant_multiply = num1 * num2
    print(resultant_multiply)
elif operation == 4:
    resultant_div = num1 / num2
    print(resultant_div)
elif operation==5:
    num_sqrt = input("enter the number to be square root")
    num_root = int(num_sqrt)
    num = math.sqrt(num_root)
    print(num)
else:
    print("Invaild")



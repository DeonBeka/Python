

from module7.main import result

num1_input = float(input("Write a float number"))
num2_input = float(input("Write another float number"))
operator_input = input("Choose an operation (+, -, *, /): ")

if operator_input == "+":
    result = num1_input + num2_input
    print(result)
elif operator_input == "-":
    result = num1_input - num2_input
    print(result)
elif operator_input == "*":
    result = num1_input * num2_input
    print(result)
elif operator_input == "/":
    result = num1_input / num2_input
    print(result)
else:
    print("error")

try:
    result = num1_input/num2_input
except ZeroDivisionError:
    print("THERE is an error")

try:
    num1 = float(num1_input)
    num2 = float(num2_input)
except ValueError:
    print("Invalid number input.")

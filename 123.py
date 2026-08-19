from operator import add,subtract,multiply,divide

print ('Simple Calculator\n')

num1 = float(input('Enter first number :'))
num2 = float(input('Enter second number :'))

operation = input("Enter operations(+,-,*,/):")

if operation =="+":
    print(add(num1,num2))
elif operation =="-":
    print(subtract(num1,num2))
elif operation =="*":
    print(multiply(num1,num2))
elif operation =="/":
    print(divide(num1,num2))
else:
    print("Invalid Operation")
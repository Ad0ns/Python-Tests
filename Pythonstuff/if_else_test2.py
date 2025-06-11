number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

biggest_num = number1

if number2 > biggest_num:
    biggest_num = number2

if number3 > biggest_num:
    biggest_num = number3
    
    
print ("the biggest number is ", biggest_num)
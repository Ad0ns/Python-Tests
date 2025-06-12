largest_number = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue #this if happens skips whole while loop here and continues onthe next if 
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number or type -1 to end the program: "))
    
#here

if counter:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")


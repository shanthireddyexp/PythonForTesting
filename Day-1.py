# Read two numbers from the keyboard and print minimum value

a = int(input("Enter the first number: "))
b= int(input("Enter the second number: "))
min = a if a<b else b
print ("Minimum value: ",min)

# Read three numbers from the keyboard and print minimum value

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
min = a if a<b else b if b<c else c
print ("Minimum value: ",min)



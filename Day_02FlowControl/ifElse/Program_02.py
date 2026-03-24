firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))
thirdNumber = int(input("Enter third number: "))

if firstNumber > secondNumber and firstNumber > thirdNumber:
    print(firstNumber, "is greater than", secondNumber, "and", thirdNumber)
elif secondNumber > firstNumber and secondNumber > thirdNumber:
    print(secondNumber, "is greater than", firstNumber, "and", thirdNumber)
else:
    print(thirdNumber, "is greater than", firstNumber, "and", secondNumber)

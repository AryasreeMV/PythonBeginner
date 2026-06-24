number = input("Enter a number : ")
# Get length of the input number
length = len(number)

result = 0
# Convert input value into integer
num = int(number)

# Iterating through the number until the last digit
while(num>0):
    result = result + (num % 10) ** length
    num = num//10

# Since num is now 0 use the variable 'number' to compare with 'result'

if(str(result)==number):
    print(f"{number} is Armstrong!")
else:
    print(f"{number} is not Armstrong!")

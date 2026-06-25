# Coding Challenge: Armstrong Number Checker

# Problem Statement:
# Write a Python program to check whether a given number is an Armstrong number or not.

# 👉 A number is called an Armstrong number (also known as a narcissistic number) if the sum of its digits each raised to the power of the number of digits is equal to the number itself.

print("<----------Armstrong Number-------->")
number = input("Enter a number to check : ")
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
    print(f"{number} is Armstrong!\n")
else:
    print(f"{number} is not Armstrong!\n")


# ⚡ Challenge Extension (Optional):
# Write a program that prints all Armstrong numbers in a given range.
print("<----------Armstrong Number Series-------->")

start = int(input("Enter the start : "))
stop = int(input("Enter the limit : "))

if(start>stop):
    print("Start number must be less than the limit")
    start = int(input("Enter the start : "))
    stop = int(input("Enter the limit : "))

print(f"Armstrong numbers between {start} and {stop} are :")

armstr_numbers = []

for i in range (start, stop+1):
    length = len(str(i))
    result = 0
    number = i
    while(i>0):
        result = result + (i % 10) ** length
        i = i//10

    if(result==number):
        armstr_numbers.append(number)

if len(armstr_numbers) == 0:
    print("There are armstrong numbers!!!")
else:
    print(armstr_numbers)
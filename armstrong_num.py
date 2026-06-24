number = input("Enter a number : ")

power = len(number)
arm = 0
num = int(number)
while(num>0):
    # print(f"ARM : {arm}")
    # print(f"Num : {num}")
    # print("Power : ", power)
    arm = arm + (num % 10) ** power
    num = num//10

if(str(arm)==number):
    print(f"{number} is Armstrong!")
else:
    print(f"{number} is not Armstrong!")

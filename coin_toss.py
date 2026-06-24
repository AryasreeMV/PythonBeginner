import random

# result = ["Head", "Tail"]

# while(True):
#     ch = int(input("1. Toss the coin?\n2.Exit\n"))
#     if(ch==1):
#         val = random.choice(result)
#         print("You got a ", val)
#     else:
#         break


res = random.randint(1,2)

print("You got Heads!") if res == 1 else print("You got Tails")
for i in range(8):
    for j in range(8):
        if(i%2!=0):
            if(j%2==0):
                print("B", end=" ")
            else:
                print("W", end=" ")
        else:
            if(j%2==0):
                print("W", end=" ")
            else:
                print("B", end=" ")
    print()
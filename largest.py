'''
# find largest and smallest numer from a list
a = [100,-6,589,10,2,3,-999,18,23,9]
# without using
print(max(a))
print(min(a))

'''

a = [100,-6,589,10,2,3,-999,18,23,9]

large = a[0]

small = a[0]


length = len(a)

for i in range(length):
    if(large < a[i]):
        large = a[i]
    if(small>a[i]):
        small = a[i]

print(f"Largest number = {large}\nSmallest number = {small}")

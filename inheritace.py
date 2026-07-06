'''
<<------- Single Inheritance -------->>
'''

# class Person1:
#     def __init__(self):
#         pass
#     def read(self):
#         print("He can read!")
#     def write(self):
#         print("He can write!")
    
# class Person2(Person1):
#     def __init__(self):
#         pass
#     def jump(self):
#         print("He can jump!!!")
#     def run(self):
#         print("He can run!!!")


# p1 = Person2()

# p1.write()
# p1.jump()


'''
--------------------- MULTI LEVEL INHERITANCE------------------
'''

# class Person1:
#     def __init__(self):
#         pass
#     def read(self):
#         print("He can read!")
#     def write(self):
#         print("He can write!")
#     def speak(self):
#         print("person 1 can speak!")
    
# class Person2(Person1):
#     def __init__(self):
#         pass
#     def jump(self):
#         print("He can jump!!!")
#     def run(self):
#         print("He can run!!!")
#     def speak(self):
#         print("person 2 can speak!")

# class Person3(Person2):
#     def __init__(self):
#         pass
#     def fly(self):
#         print("He can fly!!!")
#     def swim(self):
#         print("He can swim!!!")
#     def speak(self):
#         print("person 3 can speak!")
#         # super().speak()

# class Person4(Person3):
#     def __init__(self):
#         pass
#     def eat(self):
#         print("He can eat!!!")
#     def sleep(self):
#         print("He can sleep!!!")
#     def speak(self):
#         print("person 4 can speak!")
#         super().speak()


# p4 = Person4()

# # p4.fly()
# # p4.sleep()
# # p4.read()
# p4.speak()      # By default it invokes the speak() of class Person4



'''
<<------- Multiple Inheritance -------->>
'''

class Person1:
    def __init__(self):
        pass
    def read(self):
        print("He can read!")
    def write(self):
        print("He can write!")
    def speak(self):
        print("person 1 can speak!")
    
class Person2():
    def __init__(self):
        pass
    def jump(self):
        print("He can jump!!!")
    def run(self):
        print("He can run!!!")
    def speak(self):
        print("person 2 can speak!")

class Person3(Person2):
    def __init__(self):
        pass
    def fly(self):
        print("He can fly!!!")
    def swim(self):
        print("He can swim!!!")
    def speak(self):
        print("person 3 can speak!")
        # super().speak()

class Person4(Person2,Person1,Person3):     # "Person4 consideres Person2 as immediate super class" and it's called MRO - Method Resolution Order
    def __init__(self):
        pass
    def eat(self):
        print("He can eat!!!")
    def sleep(self):
        print("He can sleep!!!")
    # def speak(self):
    #     print("person 4 can speak!")
        # super().speak()


p4 = Person4()
p4.speak()      # By default it invokes the speak() of class Person4 if there


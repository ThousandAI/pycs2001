# Module
def say_hello(guest):
    print(f"Hello {guest}")

def introduce(name,age,gender):
    print(f"Hello my name is: {name}, age is: {age}, gender is: {gender}")

def get_max(number):
    return max(number)

def get_distance(point1,point2):
    return ((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)**(1/2)
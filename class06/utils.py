# Module
def say_hello(guest):
    print(f"Hello {guest}")

def introduce(name,age,gender):
    print(f"Hello my name is: {name}, age is: {age}, gender is: {gender}")

def get_max(numbers):
    return max(numbers)

def get_distance(point1,point2):
    return ((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)**(1/2)

if __name__ == "__main__":
    print("Hello")
    print(f"This is utils.py: {__name__}")
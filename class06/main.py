# Module
"""
import utils

number = [30,60,50,80,100,57,90]
utils.say_hello("Thousand")
utils.introduce(name="Thousand",age=30,gender="Male")

print(utils.get_max(number=number))
print(utils.get_distance(point1=(3,5),point2=(6,1)))
"""
# Package
import helper.show as show
import helper.calculate as calculate
number = [30,60,50,80,100,57,90]
show.say_hello(guest="Thousand")
show.introduce(name="Thousand",age=30,gender="Male")
print(calculate.get_max(number=number))
print(calculate.get_distance(point1=(3,5),point2=(6,1)))

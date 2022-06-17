import random
"""
#import random as r
from random import randint
#sample = random.randint(1,100)
#sample = r.randint(1,100)
sample = randint(1,100)
print(sample)

# practice
n = int(input())
for i in range(n):
    print(randint(1,100),end=" ")

"""
# lambda
"""
add = lambda x: x+3
print(add(3))
print((lambda x: x+3)(3))

mul = lambda x,y: x*y
print(mul(3,5))
"""

"""
# filter
import random
scores = [random.randint(1,100) for i in range(10)]
print(f"原始分數: {scores}")
new_scores = list(filter(lambda x: x>=60 ,scores))
print(f"篩選後的分數: {new_scores}")
new_scores = list(map(lambda x: int(x*0.7+30),scores))
print(f"調整後的分數: {new_scores}")
new_scores = sorted(scores, key=lambda x: x)
print(f"排序後的分數: {new_scores}")
"""


# def add(x):
#     return x + 3


# add = lambda x: x + 3
# print(add(10))

numbers = []
for i in range(10):
    numbers.append(random.randint(1,100))
print(f"原始: {numbers}")

new_numbers = list(filter(lambda s:s>=60,numbers))
print(f"篩選後: {new_numbers}")

new_numbers = []
for v in numbers:
    if v >= 60:
        new_numbers.append(v)



# infinite loop
"""
while True:
    x = input()
    if x == 'Q' or x == 'q':
        break
    print(x)
"""
# continue
"""
x = 0
while x <= 10:
    x += 1
    if x == 3:
        continue
    print(x,end=" ")
"""

# for i in range(0,6,1):
#     print(i)

# practice1
# n = int(input())
# for i in range(1,n+1,1):
#     print(i,end=" ")

# practice2
# n = int(input())
# for i in range(n,-1,-1):
#     print(i,end=" ")

# practice3
# sum_ = 0
# n = int(input())
# for i in range(1,n+1,1):
#     sum_ += i
# print(sum_)

# practice4
# n = int(input())
# sum_ = 0
# for i in range(n):
#     tem = int(input())
#     sum_ += tem
# print(sum_)

# 串列 list
"""
numbers = [3,5,6,10,2,8]
print(numbers)
print(numbers[0])
print(numbers[3])
print(len(numbers))
print(numbers[-1])
print(numbers[1:3])
print(numbers[:3])
print(numbers[3:])
print(numbers[-3:])
print(numbers[:])
"""

# list methods
"""
numbers = [3,5,6,10,2,8]
print(numbers)
numbers.append(15)
print(numbers)
numbers.insert(4,5)
print(numbers)
numbers.pop()
print(numbers)
numbers.remove(5)
print(numbers)
numbers.reverse()
print(numbers)
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
"""

num1 = [1,2,3,4,5,6]
num2 = num1
num3 = num1[:]
num4 = num1.copy()
num1.append(7)
num2.append(8)
num3.append(10)
num4.append(15)
print(f"num1: {num1}, num2: {num2} ,num3: {num3}, num4: {num4}")


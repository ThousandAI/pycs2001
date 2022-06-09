# dictionary
"""
dic = {"sports":["Basketball","Volleyball"],"name":["Allie","Thousand"]}
print(dic)
print(dic["sports"])
print(dic["sports"][0])

dic["scores"] = [70,50.2,95.8]
print(dic)
"""

"""
# for + list

# practice1
nums = [30,50,80,90,100,20,60,90,100,20,80,50]  # 0-11 len:12
for i in range(len(nums)):
    print(nums[i],end=" ")
print()
# practice2
for i in range(len(nums)-1,-1,-1):
    print(nums[i],end=" ")
print()
#practice3
member = []
n = int(input())
for i in range(n):
    member.append(int(input()))
print(f"member: {member}")
#practice4
print(f"總和: {sum(member)} 最大值: {max(member)} 最小值: {min(member)}")
"""
# for + list (另一種做法)
"""
scores = [70,30,60,80,100,50,90,20,60,10,30,80]
for value in scores:  # iterable
    print(value,end=" ")
"""


"""
# string
name = "thousand"
print(name[0])
print(len(name))

print(name.lower())
print(name.upper())
print(name.islower()) # 全部
print(name[0].islower())
print(name[0].isupper())

# practice1
score = input()
print(score) # "2 3 6 8 10"
print(score.split()) # ["2","3","6","8","10"]
score = score.split()
for i in range(len(score)):
    score[i] = int(score[i])
print(f"轉型後的串列: {score}")
"""

# name = "Allie"
# for v in name:
#     print(v,end=" ")
#
# code = input()
# count = 0
# for v in code:
#     if v == "a":
#         count += 1
# print(f"a 的次數: {count}")

# 使用者輸入n，產生 n 個 0 的串列，輸入: 6 => 輸出: [0,0,0,0,0,0]
# n = int(input())
# scores = []
# for i in range(n):
#     scores.append(0)
# print(scores)
"""
scores = [i for i in range(int(input())) if i % 2 == 0]
print(scores)

# 相當於
scores = []
for i in range(int(input())):
    if i % 2==0:
        scores.append(i)
print(scores)
"""
# function
"""
xxx = 3
def say_hello():
    print("Hello")
    print(xxx)

def add_numbers(num1,num2,num3):
    #print(num1+num2+num3)
    return num1+num2+num3

say_hello()

# s = add_numbers(3,5,7)
# print(s)

def get_mean(numbers):
    total = 0
    for v in numbers:
        total += v
    return total/len(numbers)

num = [1,2,3]
mean = get_mean(numbers= num)
print(mean)
"""



# dictionary
n = int(input())
dic = {}
for i in range(n):
    s = input().split()
    dic[s[0]] = int(s[1])
print(dic)


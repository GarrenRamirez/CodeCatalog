import copy

num1 = 10
num2 = copy.deepcopy(num1)

print(num1)
print(num2)
print(id(num1))
print(id(num2))

num1 = 11

print(num1)
print(num2)
print(id(num1))
print(id(num2))

num3 = ["Apples", "Oranges", "Banaenaes"]
num4 = num3

print(num4)
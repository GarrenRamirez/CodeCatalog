"""
age = int(input("Enter your age: "))
num2 = input("Enter another number: ")
num2 = float(num2)
height = 7.2
name = "Garren :D"
is_student = True

"""
"""
num1 = 21
num2 = 2
print(num1%num2)

#print("Type of age is: ", type(age))
#print(age + num2)
#print("Type of height is: ", type(height))
#print(name)
#print(is_student)

"""
"""
string1 = "This is a big string with lots of words!"
print(string1.upper())
print(string1.lower())
print(string1.find("words"))
print(string1.replace("big", "small"))

"""
"""
num = int(input("Enter number: "))

if num > 0:
    print("+")
elif num == 0:
    print("0")
else :
    print("-")

print("Loop: ")
for i in range (1, 11):
    print(i)

"""

dimensions = (200,50,100,40,40,40)
print(dimensions[3])
a,b,c,d,e,f = dimensions

print("Loop with tuple: ")
for i in dimensions:
    print(i)

print(200 in dimensions)
print(45 in dimensions)

sorted_tuple=sorted(dimensions)
print(type(dimensions))
print(type(sorted_tuple))

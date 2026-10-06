# Introduction to Python - Module 1

# 1. Variables
name = "Manish"
age = 19
course = "AIML"

print("Name:", name)
print("Age:", age)
print("Course:", course)


# 2. Basic calculations
a = 10
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)


# 3. List
numbers = [10, 20, 30, 40, 50]

print("Numbers:", numbers)
print("First number:", numbers[0])


# 4. For loop
print("Numbers using loop:")

for number in numbers:
    print(number)


# 5. Function
def greet(name):
    print("Hello", name)

greet("Manish")


# 6. Simple condition
marks = 75

if marks >= 40:
    print("Pass")
else:
    print("Fail")

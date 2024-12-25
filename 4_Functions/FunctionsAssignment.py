# What does the len() function do in Python? Write a code example using len() to find the length of a list.
# l1=[1,2,3,4,5,6,7,8,9]
# length=len(l1)
# print("The length of list is:",length)

# Write a Python function greet(name) that takes a person's name as input and prints "Hello, [name]!".
# def greet(name):
#     print("Hello",name)
# greet("swetha")

# Write a Python function find_maximum(numbers) that takes a list of integers and returns the maximum value without using the built-in max() function.
# Use a loop to iterate through the list and compare values.
# numbers=[]
# def find_maximum(numbers):
#     max=numbers[0]
#     for i in numbers:
#         if i>max:
#             max=i
#     print(max)
# find_maximum([56,90,76,12,100])

# Explain the difference between local and global variables in a Python function.
# Write a program where a global variable and a local variable have the same name and show how Python differentiates between them.
"""
Local Variable: A variable declared inside a function whose scope is limited to the function in which it is defined.
It cannot be accessed outside the function
Global Variable:A variable declared outside any function which can be accessed and modified throughout the program (including inside
functions) unless shadowed by a local variable of the same name.To modify a global variable inside a function,
you need to use the global keyword.
"""
# v=10
# def fn():
#     v=20
#     print("Local variable(v) inside function:",v)
# print("Global variable(v) outside function:",v)
# fn()

# Create a function calculate_area(length, width=5) that calculates the area of a rectangle.
# If only the length is provided, the function should assume the width is 5.
# Show how the function behaves when called with and without the width argument.
"""
The width parameter has a default value of 5. If the caller does not provide a value for width, the function assumes it is 5.
When both length and width are provided, the function uses those values.
"""
# def calculate_area(length, width=5):
#     area=length*width
#     return area
# answer1=calculate_area(4)
# print("Area(Without width argument):",answer1)
# answer2=calculate_area(4,10)
# print("Area(With width argument):",answer2)

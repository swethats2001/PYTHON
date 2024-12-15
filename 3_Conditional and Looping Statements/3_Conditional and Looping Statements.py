# A certain cinema currently sells tickets for a full price of 6 pounds,
# but always sells tickets for half price to people who are less than 16 years old,
# and for a third of the price for people who are 60 years old or more.
# tkt=6.00
# age=int(input("Enter your age: "))
# if age<16:
#     print("Your ticket costs: £",tkt//2)
# elif age>=60:
#     print("Your ticket costs: £", tkt//3)
# else:
#     print("Your ticket costs: £", tkt)

# Write a Python program to receive 3 numbers from the user and print the greatest among them.
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# c=int(input("Enter third number: "))
# if a>b and a>c:
#     print(a," is the greatest number")
# elif b>c:
#     print(b," is the greatest number")
# else:
#     print(c, " is the greatest number")

# Find the factorial of a given number using loops(note the number is received from the user)
# num=int(input("Enter a number: "))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print(fact)

# Reverse a number using while loop
# num=int(input("Enter a number with 2 or more digits: "))
# rev=0
# while num>0:
#     dig=num%10
#     rev=rev*10+dig
#     num=num//10
# print("Reversed number: ",rev)

# Finding the multiples of a number using loop
# num=int(input("Enter a number: "))
# print("The multiples of {} are:".format(num),end=" ")
# for i in range(1,11):
#     print(i*num,end=" ")

# Write a program to print the inputted value as it is and break the loop if the value is 'done'.
# value=input("Enter any word: ")
# while True:
#     print(value)
#     if value.lower()=="done":
#         break

# Write a program that prints the numbers from 1 to 10. But for multiples of three print "Fizz" instead of the number and for the multiple of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz"
# for i in range(1,11):
#     if i%3==0 and i%5 ==0:
#         print("FizzBuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     else:
#         print(i)

# Write a program to print the following pattern:
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
# for i in range(5,0,-1):
#     while i>0:
#         print(i,end=" ")
#         i=i-1
#     print()



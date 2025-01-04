# Exercise 1: (score : 1) Write a Python program to read a file and display its contents
# file1=open("FHass.txt",'r')
# print(file1.read())

# Exercise 2: (score : 1) Write a Python program to copy the contents of one file to another file
# with open('FHass.txt', 'r') as file1, open('FHass2.txt', 'w') as file2:
#     file2.write(file1.read())
# file3=open("FHass2.txt",'r')
# print(file3.read())

# Exercise 3: (score : 2) Write a Python program to read the content of a file and count the total number of words in that file.
# file1 = open("FHass.txt", 'r')
# content = file1.read()
# print(content)
# print("Total number of words:", len(content.split()))

# Exercise 4: (score : 1) Write a Python program that prompts the user to input a string and converts it to an integer.
# Use try-except blocks to handle any exceptions that might occur
# str=input("enter string which is to be converted to int:")
# try:
#     cstr=int(str)
#     print("The string converted to integer:",cstr)
# except Exception:
#     print("This string cannot be converted to integer")

# Exercise 5: (score : 1) Write a Python program that prompts the user to input a list of integers and raises an exception if any of the
# integers in the list are negative.
# try:
#     l1 = list(map(int, input("Enter a list of integers: ").split()))
#     for i in l1:
#         if i<0:
#             raise ValueError("Negative integer found",i)
# except ValueError as e:
#         print(f"Error: {e}")

# Exercise 6: (score : 2) Write a Python program that prompts the user to input a list of integers and computes the average
# of those integers. Use try-except blocks to handle any exceptions that might occur.use the finally clause to print a message
# indicating that the program has finished running.
# try:
#     numbers = list(map(int, input("Enter a list of integers: ").split()))
#     average = sum(numbers) / len(numbers)
#     print(f"The average is: {average}")
# except ValueError:
#     print("Error: Please enter only integers.")
# finally:
#     print("Thank you.")

# Exercise 7 : (score : 2) Write a Python program that prompts the user to input a filename and writes a string to that file.
# Use try-except blocks to handle any exceptions that might occur and print a welcome message if there is no exception occurred.
try:
    filename = input("Enter the filename: ")
    with open(filename, 'w') as file:
        file.write("Welcome to file handling in Python!\n")
        print(f"String written to file successfully!")
except Exception as e:
    print(f"An error occurred: {e}")




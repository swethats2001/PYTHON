# Write a program that asks the user to enter an amount in pounds (£) and the program calculates and converts an amount in dollar ($)
pounds=int(input("Enter an amount in pounds (£): "))
dollar=1.36 * pounds
print("Amount in Dollars($): ",round(dollar,2))
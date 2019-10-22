# Program 4-8 Sum Of Numbers
# Shaun Hayworth
# CIS 2
# 10-22-2019
# Original source code and revision history can be found at https://github.com/SCHayworth/4-8-Sum-Of-Numbers

# Gets a series of positive numbers from the user and adds them all together.
# Entering a negative number signals the end of the sequence.

# Initialize the total with a value of 0
total = 0

# Prompts the user for the first number
number = input('Enter a positive number (negative to quit): ')

# Loops while the number is positive
while number > 0:
    total += number

    # Prompt user for the next number in the sequence
    number = input('Enter a positive number (negative to quit): ')

# Prints the total
print(f'Total = {total}')

# Scope
Write a program with a loop that asks the user to enter a series of positive numbers. The user should enter a negative number to signal the end of the series. After all the positive numbers have been entered, the program should display their sum.

### Example Run
    Enter a positive number (negative to quit):  5
    Enter a positive number (negative to quit):  4
    Enter a positive number (negative to quit):  8
    Enter a positive number (negative to quit):  7
    Enter a positive number (negative to quit):  2
    Enter a positive number (negative to quit):  -2
    Total = 26.00
# Pseudocode
    START
    set total = 0
    Prompt user for the first number or a negative number to quit
    WHILE number is positive
      add number to Total
      prompt user for the next number to total
    Print total
    END

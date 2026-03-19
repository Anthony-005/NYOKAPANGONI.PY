# BASIC SYNTAX

try:
    result = 3/0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# USING AN generic except(LEAVE THIS ALONE DURING EXAMS)
try:
    result = 3/0
except Exception as e:
    print(f"Error occured: {e}")



# handling different errors separately
try:
    num=int(input("Enter a number:"))
    result = 10/ num
except ValueError:
    print("Invalid input! Enter a number!!")
except ZeroDivisionError:
    print("Cannot be divided by zero!")

print(f"The result is {result}")
print("SUCCESSFUL EXECUTION, HAVE A NICE DAY")


# Raising exceptions Manually

def withdraw(amount):
    if amount<0 :
        raise ValueError("An amount cannot be negative")
    else:
        print("The amount withdrawn is {amount}")

try:
    withdraw(-20000)
except ValueError:
    print("Transaction failed!")






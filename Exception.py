try:
    # Asking user for input
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    
    # Attempting division
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input! Please enter a number.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print(f"The result is: {result}")
finally:
    print("Execution completed.")

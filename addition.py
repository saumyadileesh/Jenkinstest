import os
# This is a simple Python script to add two numbers
num1 = os.environ.get('num1')
num2 = os.environ.get('num2')
# Perform the addition
sum_result = num1 + num2

# Print the result
print(f"The sum of {num1} and {num2} is: {sum_result}")

import sys
 
# Fetch the single string parameter from Jenkins
input_values = sys.argv[1]
 
# Split the string into individual numbers (e.g., "5 3" -> [5, 3])
num1, num2 = map(int, input_values.split())
 
# Perform addition
result = num1 + num2
 
# Print the result
print(f"The sum of {num1} and {num2} is {result}")

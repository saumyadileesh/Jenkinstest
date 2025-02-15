import sys
 
# Check if arguments are passed

if len(sys.argv) != 3:

    print("Usage: python3 test.py <num1> <num2>")

    sys.exit(1)
 
# Convert arguments to numbers

num1 = float(sys.argv[1])

num2 = float(sys.argv[2])
 
# Perform addition

result = num1 + num2
 
print(f"Addition result: {result}")
 

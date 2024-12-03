# Create a list of 10 numbers
numbers = [1, 5, 8, 12, 7, 3, 14, 10, 9, 6]

# Calculate the sum of the numbers in the list
total_sum = sum(numbers)

# Print the list and the sum
print("List of numbers:", numbers)
print("Sum of numbers:", total_sum)

# Initialize an empty list to store the reversed numbers
reversed_numbers = []

# Use a for loop to iterate through the list in reverse order
for i in range(len(numbers)-1, -1, -1):
    reversed_numbers.append(numbers[i])

# Print the original and reversed lists
print("Original List:", numbers)
print("Reversed List:", reversed_numbers)
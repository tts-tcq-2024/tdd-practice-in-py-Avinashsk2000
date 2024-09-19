import sys

def validate_number(num):
    return num if num <= 1000 else 0  # Ignore numbers greater than 1000

# Function to check for negative numbers and raise an exception if found
def find_negatives(numbers):
    negative_numbers = list(filter(lambda n: n < 0, numbers))
    if negative_numbers:
        raise ValueError(f"Negative numbers are not allowed")

# Function to sum valid numbers from tokens
def calculate_sum(tokens):
    numbers = list(map(int, tokens))  # Convert all tokens to integers using map
    find_negatives(numbers)
    return sum(validate_number(num) for num in numbers) 

# Function to extract and apply a custom separator
def detect_custom_separator(input_data):
    if input_data.startswith("//"):
        separator = input_data[2]
        return separator, input_data.split('\n', 1)[1]
    return ',', input_data  # Default separator: comma

# Main function to process the input and return the sum
def add(input_data):
    if not input_data:
        return 0

    # Get the separator and numbers
    separator, number_section = detect_custom_separator(input_data)

    # Split and sum the numbers
    tokens = number_section.replace('\n', separator).split(separator)
    return calculate_sum(tokens)

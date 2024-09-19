import sys

# Raise an exception if negative numbers are found
def check_for_negatives(values):
    negatives = [n for n in values if n < 0]
    if negatives:
        raise ValueError(f"Negative numbers are not allowed")

# Check if a number is valid (<= 1000)
def is_valid(number):
    return number if number <= 1000 else 0  
    
# Calculate the sum of valid numbers
def compute_total(parts):
    values = [int(part) for part in parts]  # Convert strings to integers
    check_for_negatives(values) 
    return sum(is_valid(n) for n in values)  

# Extract custom delimiter if present
def get_custom_separator(input_str):
    if input_str.startswith("//"):
        delimiter = input_str[2]
        return delimiter, input_str.split('\n', 1)[1]
    return ',', input_str  # Default delimiter: comma

# Main function to handle input and calculate the sum
def add(input_str):
    if not input_str:
        return 0

    delimiter, data = get_custom_separator(input_str)
    parts = data.replace('\n', delimiter).split(delimiter)
    return compute_total(parts)

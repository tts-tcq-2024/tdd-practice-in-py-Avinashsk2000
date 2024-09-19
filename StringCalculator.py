import sys
from functools import reduce

# Use a function to replace conditionals for validating numbers
def valid_if_less_than_1000(num):
    return num * (num <= 1000) 

# Function to raise an exception if negative numbers are found
def raise_if_negatives_present(values):
    negatives = list(filter(lambda x: x < 0, values))  # Use filter to find negative numbers
    if negatives: 
        raise ValueError(f"Negative numbers are not allowed")

# Function to sum numbers using reduce, replacing explicit loops
def sum_valid_numbers(parts):
    values = list(map(int, parts)) 
    raise_if_negatives_present(values)  
    return reduce(lambda total, num: total + valid_if_less_than_1000(num), values, 0)

# Function to get custom separator using slicing, avoiding conditionals
def parse_custom_separator(input_str):
    return (input_str[2], input_str.split('\n', 1)[1]) if input_str.startswith("//") else (',', input_str)

# Main function to handle input and calculate the sum
def add(input_str):
    if not input_str:
        return 0  
    separator, data = parse_custom_separator(input_str)  
    parts = data.replace('\n', separator).split(separator)
    return sum_valid_numbers(parts) 

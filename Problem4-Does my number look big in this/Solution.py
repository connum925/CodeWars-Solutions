import math

def narcissistic(value):
    # Handle edge case: 0 is not narcissistic
    if value == 0:
        return True
    
    # Calculate number of digits using logarithm
    size = math.floor(math.log10(abs(value))) + 1
    
    sum = 0
    aux_value = value
    
    # Extract each digit from right to left
    while aux_value > 0:
        digit = aux_value % 10  # Get last digit
        sum = sum + (pow(digit, size))  # Add digit^size to sum
        aux_value //= 10  # Remove last digit
    
    # Check if sum equals original value
    if sum == value:
        return True
    return False
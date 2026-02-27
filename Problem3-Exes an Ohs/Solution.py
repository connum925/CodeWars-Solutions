def xo(s):
    # Initialize counters for 'o' and 'x'
    count_o = 0
    count_x = 0
    
    # Iterate through each character in the string
    for letter in s:
        letter = letter.lower()
        # Count occurrences of 'o'
        if letter == "o":
            count_o += 1
        # Count occurrences of 'x'
        elif letter == "x":
            count_x += 1
    
    print(count_o)
    print(count_x)
    
    # Return True if counts are equal
    if count_o == count_x:
        return True
    elif (count_o and count_x) == 0:
        return False
    else:
        return False
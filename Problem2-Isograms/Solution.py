def is_isogram(string):
    #Create an empty set to store letters we have already seen
    #A set allows O(1) search and insertion operations
    List=set()
    # Iterate through each letter in the string
    string = string.lower()
    for letter in string:
        # Check if the letter (in lowercase) already exists in the set
        # We convert to lowercase so 'A' and 'a' are treated as the same letter
        if letter in List:
            # If the letter already exists, there are duplicates → not an isogram
            return False
        else:
            # If the letter doesn't exist, add it to the set
            List.add(letter)
    # If we finished the loop without finding duplicates → it's an isogram
    return True

"""
Example:
print(is_isogram("XWYvZiCBQmCWukD"))
"""
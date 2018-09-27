

def is_isogram(string):
    # extract letters and lowercase them
    chars = [c.lower() for c in string if c.isalpha()]
    # eliminate any duplicates and compare the size of strings
    return len(set(chars)) == len(chars)

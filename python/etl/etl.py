def transform(legacy_data):
    new_letters = {}
    for points, letters in legacy_data.items():
        for letter in letters:
            new_letters[letter.lower()] = points
    return new_letters

def vowel_filter(function):

    def wrapper():
        letters = function()
        result = []

        for letter in letters:
            if letter in "aoueiy":
                result.append(letter)
        return result

    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

@vowel_filter
def get_another_letters():
    return ["b", "c", "e"]

print(get_letters())
print(get_another_letters())
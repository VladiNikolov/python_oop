def type_check(type):

    def decorator(function):

        def wrapper(arg):

            if not isinstance(arg, type):
                return "Bad Type"

            return function(arg)

        return wrapper

    return decorator


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))


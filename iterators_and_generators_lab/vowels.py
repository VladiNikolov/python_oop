class vowels:
    ALL_VOWELS = "AEIUYOaeiuyo"

    def __init__(self, text: str):
        self.text = text
        self.vowels_in_text = []
        for el in self.text:
            if el in vowels.ALL_VOWELS:
                self.vowels_in_text.append(el)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.vowels_in_text:
            raise StopIteration

        return self.vowels_in_text.pop(0)


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
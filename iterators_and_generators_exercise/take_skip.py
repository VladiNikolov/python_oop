class take_skip:

    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= 0:
            raise StopIteration

        result = self.num * self.step
        self.count -= 1
        self.num += 1

        return result

numbers = take_skip(2, 6)
for number in numbers:
    print(number)




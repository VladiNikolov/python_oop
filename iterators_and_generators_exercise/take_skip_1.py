class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.iteration = - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.iteration == self.count - 1:
            raise StopIteration

        self.iteration += 1

        return self.iteration * self.step

numbers = take_skip(2, 6)
for number in numbers:
    print(number)




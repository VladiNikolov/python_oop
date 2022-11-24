class countdown_iterator:

    def __init__(self, count: int):
        self.count = count + 1
        self.iteration = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= self.iteration:
            raise StopIteration

        result = self.count - 1
        self.count -= 1

        return result

iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

import time

class exec_time:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args):
        start = time.time()
        self.function(*args)
        end = time.time()

        return end - start

@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total

print(loop(1, 10000000))

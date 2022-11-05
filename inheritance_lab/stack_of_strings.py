class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        last_element = self.data.pop()
        return last_element

    def top(self):
        top_element = self.data[-1]
        return top_element

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return f'[{", ".join(reversed(self.data))}]'




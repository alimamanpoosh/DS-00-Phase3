class Stack:

    def __init__(self, capacity):
        self.top = 0
        self.capacity = capacity

        self.array = []

    def isEmpty(self):
        return self.top == 0

    def peek(self):
        return self.array[self.top - 1]

    def pop(self):
        if self.top == self.capacity:
            raise Exception()
        self.top -= 1
        return self.array.pop()

    def push(self, op):
        self.top += 1
        self.array.append(op)

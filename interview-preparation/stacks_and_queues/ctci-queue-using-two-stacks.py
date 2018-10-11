class MyQueue(object):
    def __init__(self):
        self.newest = []
        self.oldest = []

    def peek(self):
        self.shift_stacks()
        return self.oldest[-1]

    def pop(self):
        self.shift_stacks()
        return self.oldest.pop()

    def shift_stacks(self):
        if not self.oldest:
            while self.newest:
                self.oldest.append(self.newest.pop())

    def put(self, value):
        self.newest.append(value)

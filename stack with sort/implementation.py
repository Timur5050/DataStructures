class Stack:
    def __init__(self):
        self.stack = []
        self._size = 0

    def empty(self):
        return len(self.stack) == 0

    def size(self):
        return self._size

    def top(self):
        if self.stack:
            return self.stack[-1]

    def push(self, value):
        self.stack.append(value)
        self._size += 1

    def pop(self):
        if self.stack:
            self.stack.pop()
            self._size -= 1




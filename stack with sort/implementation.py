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
        return "stack is empty"
    def push(self, value):
        self.__sort(value)
        self._size += 1

    def pop(self):
        if self.stack:
            self.stack.pop()
            self._size -= 1

    def __sort(self, value):
        if self._size >= 1:
            if value > self.top():
                temp_val = self.top()
                self.pop()
                self.__sort(value)
                self.stack.append(temp_val)
                self._size += 1
            else:
                self.stack.append(value)
        else:
            self.stack.append(value)



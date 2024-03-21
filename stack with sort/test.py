import implementation

test = implementation.Stack()

print(test.empty())
test.push(-1)
test.push(10)
test.push(5)
print(test.top())
test.pop()
print(test.top())

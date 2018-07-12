class Stack:
    def __init__(self):
        self._stack = None
        self._size = None

    def create_stack(self, x):
        self._stack = [x]
        self._size = 1
        return self._stack

    def is_empty(self):
        return self._size == 0

    def peek(self):
        assert self.is_empty() == False
        return self._stack[self._size-1]

    def pop(self):
        assert self.is_empty() == False
        x = self._stack.pop()
        return x

    def push(self, x):
        self._stack.append(x)


stack = Stack()
stack.create_stack(5)
print(stack.peek())

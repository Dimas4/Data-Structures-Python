def create_stack(x):
    stack = [x]
    return stack


def is_empty(stack):
    return len(stack) == 0


def peek(stack):
    assert is_empty(stack) == False
    return stack[len(stack)-1]


def pop(stack):
    assert is_empty(stack) == False
    x = stack.pop()
    return x


def push(stack, x):
    stack.append(x)


stack = create_stack(5)
print(is_empty(stack))
print(push(stack, 16))
print(peek(stack))

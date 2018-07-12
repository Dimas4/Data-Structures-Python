from collections import deque


def create_deque(x):
    queue = [x]
    queue = deque(queue)
    return queue


def enqueue_first(deque, x):
    deque.appendleft(x)


def enqueue_last(deque, x):
    deque.append(x)


def dequeue_first(deque):
    return deque.popleft()


def dequeue_last(deque):
    return deque.pop()


def peek_first(deque):
    return deque[0]


def peek_last(deque):
    return deque[len(deque)-1]


queue = create_deque(5)
enqueue_first(queue, 7)
enqueue_last(queue, 10)
print(queue)
print(peek_first(queue))
print(queue)

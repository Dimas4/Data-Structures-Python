from collections import deque


class Deque:
    def __init__(self):
        self._deque = None

    def create_deque(self, x):
        self._deque = [x]
        self._deque = deque(self._deque)
        return self._deque

    def enqueue_first(self, x):
        self._deque.appendleft(x)

    def enqueue_last(self, x):
        self._deque.append(x)

    def dequeue_first(self):
        return self._deque.popleft()

    def dequeue_last(self):
        return self._deque.pop()

    def peek_first(self):
        return self._deque[0]

    def peek_last(self):
        return self._deque[len(self._deque) - 1]

    def print_deque(self):
        print(self._deque)


deq = Deque()
print(deq.create_deque(5))
deq.enqueue_first(5)
deq.enqueue_first(7)
deq.print_deque()
print(deq.dequeue_last())
deq.print_deque()

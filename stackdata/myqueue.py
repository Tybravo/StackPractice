class Queue:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = [None] * capacity
        self.number = 0

    def is_queue_empty(self):
        return self.number == 0

    def enqueue(self, states: str):
        self.is_full()
        self.values[self.number] = states
        self.number += 1
        return True

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        head = self.index_zero()
        self.values = self.shift()
        self.number -= 1
        return self.values

    def index_zero(self):
        if self.is_empty():
            return None
        return self.values[0]

    def shift(self):
        return [self.values[i] for i in range(1, self.capacity)]

    def number_of_elements(self):
        return self.number

    def is_empty(self):
        return self.number == 0

    def is_full(self):
        if self.number == self.capacity:
            raise IndexError("Queue is full")

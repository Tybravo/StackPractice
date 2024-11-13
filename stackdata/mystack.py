from os import remove


class MyStack:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = [None] * capacity
        self.number = 0
        self.is_empty = True

    def stack_is_empty(self):
        self.is_empty = True

    def stack_is_not_empty(self):
        self.is_empty = False

    def get_is_empty(self):
        return self.is_empty

    def push(self, param):
        if self.is_full():
            raise ValueError("Stack is full")
        self.data[self.number] = param
        self.number += 1

    def pop(self):
        if self.number == 0:
            raise ValueError("Stack is empty")
        self.number -= 1

        value = self.data[self.number]
        self.data[self.number] = None
        return value



    def is_full(self):
        return self.number == self.capacity




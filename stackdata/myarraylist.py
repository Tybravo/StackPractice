
class MyArrayList:

    def __init__(self, capacity=4):
        self.capacity = capacity
        self.list = [None] * capacity
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def my_add(self, index, item):
        if self.size < self.capacity:
            for count in range(self.size, index, -1):
                self.list[count] = self.list[count - 1]
            self.list[index] = item
            self.size += 1
        else:
            print("List is full")


    def my_remove(self, index):
        if 0 <= index < self.size:
            for count in range(index, self.size - 1):
                self.list[count] = self.list[count + 1]
            self.list[self.size - 1] = None
            self.size -= 1
        else:
            print("Invalid index")

    def get(self, index):
        if 0 <= index < self.size:
            return self.list[index]
        else:
            raise IndexError(f"Index: {index}, Size: {self.size}")

    def get_size(self):
        return self.size

    def get_capacity(self):
        return self.capacity

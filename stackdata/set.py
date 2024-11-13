class Set:

    def __init__(self):
        self.my_set = set()


    def add_element(self, element):
        if element not in self.my_set:
            self.my_set.add(element)


    def get_size(self):
        count = 0
        for _ in self.my_set:
            count += 1
        return count


    def get_elements(self):
        return self.my_set


    def pop_element(self, element):
        if element in self.my_set:
            self.my_set.remove(element)
            return element
        else:
            raise KeyError("Element not found in the set")



    def update_set(self, iterable):
        # self.my_set.update(iterable)
        for element in iterable:
            if element not in self.my_set:
                self.my_set.add(element)


    def clear_all_elements(self):
        while len(self.my_set) > 0:
            element = next(iter(self.my_set)) #get the next item in the set
            self.my_set.remove(element)



    def remove_element(self, element):
        if element not in self.my_set:
            raise KeyError("Element not found in set")

        if element in self.my_set:
            self.my_set.remove(element)


    def discard(self, element):
        if element in self.my_set:
            new_items = []
            for item in self.my_set:
                if item != element:
                    new_items += [item]
            self.my_set = new_items



    def find_element(self, element):
        if element in self.my_set:
            return element
        else:
            raise KeyError(f"Element '{element}' not found in the set.")




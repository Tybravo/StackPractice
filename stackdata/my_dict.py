class MyDict:
    def __init__(self):
        self.my_dict = {}


    def set(self, dict_key, value):
        self.my_dict[dict_key] = value


    def get_key(self, dict_key):
        if dict_key in self.my_dict:
            return self.my_dict[dict_key]
        else:
            raise KeyError("Invalid key in this MyDict")


    def get_key_by_value(self, value):
        for dict_key, dict_value in self.my_dict.items():
            if dict_value == value:
                return dict_key
        raise ValueError("Value not found in this MyDict")



    def pop_key(self, dict_key):
        if dict_key in self.my_dict:
            del self.my_dict[dict_key]
        else:
            raise KeyError(f"Key '{dict_key}' not found.")



    def pop_item(self):
        if not self.my_dict:
            raise KeyError("Dictionary is empty")

        last_key, last_value = next(reversed(self.my_dict.items()))
        del self.my_dict[last_key]
        return last_key, last_value


    def get_dict_size(self):
        count = 0
        for _ in self.my_dict:
            count += 1
        return count


    def contains(self, key):
        return key in self.my_dict


    def clear(self):
        self.my_dict.clear()
        return self.get_dict_size()


    def keys_view(self):
        return self.my_dict.keys()


    def values_view(self):
        # return {key: self.my_dict[key] for key in self.my_dict}
        # return self.my_dict.values()
        return list(self.my_dict.values())



    def items_view(self):
        return list(self.my_dict.items())


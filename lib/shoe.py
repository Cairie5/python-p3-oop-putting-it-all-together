class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = size  # Use an underscore to indicate it's a private attribute
        self.condition = "Used"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    def cobble(self):
        self.condition = "New"

    def __str__(self):
        return f"Brand: {self.brand}, Size: {self.size}, Condition: {self.condition}"

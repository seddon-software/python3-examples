class Calculator:
    def add(self, x, y):
        if not isinstance(x, int):
            raise TypeError("x must be an int")
        if not isinstance(y, int):
            raise TypeError("y must be an int")
        return x + y
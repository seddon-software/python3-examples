class Calculator:
    def add(self, x, y):
        if not isinstance(x, int) : raise ValueError()
        if not isinstance(y, int) : raise ValueError()
        return x + y

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_element = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_element:
            self.min_element.append(val)
        else:
            if self.min_element[-1] >= val:
                self.min_element.append(val)

    def pop(self) -> None:
        v = self.stack.pop()
        if self.min_element[-1] == v:
            self.min_element.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_element[-1]

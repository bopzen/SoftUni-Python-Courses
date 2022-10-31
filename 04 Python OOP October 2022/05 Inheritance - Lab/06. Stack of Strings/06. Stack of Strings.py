class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return max(self.data)

    def is_empty(self):
        if self.data:
            return False
        return True

    def __str__(self):
        return f"[{', '.join(str(x) for x in reversed(self.data))}]"
# stack class
class Stack():
    # constructor
    def __init__(self):
        self.contents = []  # values inside stack
        self.top = None  # keeps track of top of stack

    # push new operators to stack
    def push(self, val):
        self.top = val  # update haed
        self.contents.append(val)  # add value to stack

    # 'pop' top off stack
    def pop(self):
        return self.contents.pop()

    # return size of stack
    def get_size(self):
        return len(self.contents)

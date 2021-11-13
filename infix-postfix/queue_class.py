# queue class
class QueueC():
    # constructor
    def __init__(self):
        self.contents = []

    # add value to back of queue
    def add(self, val):
        self.contents.insert(0, val)

    # remove value off front of queue
    def remove(self):
        return self.contents.pop()

    # return size of queue
    def get_size(self):
        return len(self.contents)

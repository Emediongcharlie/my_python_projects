class mystack:

    def __init__(self):
        self.stack = []


    def add_to_stack(self, item):
        return self.stack.append(item)

    # def pop(self):
    #     del self.stack[-1]
    #     return self.stack

    def add_to_the_beginning_of_the_stack(self, new_item):
        return self.stack.insert(0, new_item)

    # def remove(self):
    #     del self.stack[0]
    #     return self.stack
    #
    # # def add_to_beginning_of_queue(self, queue_item):
    # #     return self.queue.insert(0, queue_item)
    # #
    def pop(self):
        del self.stack[0]
        return self.stack

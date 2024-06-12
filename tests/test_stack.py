import unittest

from stack import mystack

class MyTestCase(unittest.TestCase):
    def test_stack_can_add_element(self):
        stack = mystack()
        stack.add_to_stack("semicolon.africa")
        stack.add_to_stack("google.com")
        self.assertEqual(len(stack.stack), 2)  # add assertion here

    def test_to_remove_the_last_element(self):
        stack = mystack()
        stack.add_to_stack("semicolon.africa")
        stack.add_to_stack("google.com")
        stack.pop()
        self.assertEqual((stack.stack[- 1]), "semicolon.africa")

    def test_to_add_to_the_first_element(self):
        stack = mystack()
        stack.add_to_the_beginning_of_the_stack("r.com")
        stack.add_to_the_beginning_of_the_stack("x.com")
        stack.add_to_stack("semicolon.com")
        stack.add_to_stack("google.com")
        self.assertEqual((stack.stack[1]), "r.com")

    def test_to_remove_the_first_element(self):
        stack = mystack()
        stack.add_to_stack("semicolon.africa")
        stack.add_to_stack("google.com")
        stack.pop()
        self.assertEqual((stack.stack[0]), "google.com")

    # queue

    def test_to_add_first_element_and_remove_first_element(self):
        queue = mystack()
        queue.add_to_the_beginning_of_the_stack("x.com")
        queue.add_to_stack("semicolon.com")
        self.assertEqual((queue.stack[0]), "x.com")
        queue.pop()
        self.assertEqual((queue.stack[0]), "semicolon.com")

    if __name__ == '__main__':
        unittest.main()

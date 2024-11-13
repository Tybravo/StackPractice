import unittest
from stackdata import mystack
from stackdata.mystack import MyStack


class TestStack(unittest.TestCase):
    def test_that_app_can_push_X_stack_is_not_empty(self):
        my_stack = MyStack(3)
        my_stack.push(1)
        when = my_stack.stack_is_not_empty()
        self.assertFalse(False, when)

    def test_that_app_can_push_A_and_pop_A_stack_is_empty(self):
        my_stack = MyStack(3)
        self.assertTrue(True, my_stack.stack_is_empty())
        my_stack.push(1)
        self.assertTrue(True, my_stack.stack_is_not_empty())
        my_stack.pop()
        self.assertTrue(True, my_stack.stack_is_not_empty())

    def test_that_app_can_pop_from_stack(self):
        my_stack = MyStack(3)
        my_stack.push(1)
        my_stack.push(2)
        value = my_stack.pop()
        self.assertEqual(value, 2)
        self.assertEqual(my_stack.number, 1)
        self.assertEqual(my_stack.data[1], None)

    def test_that_stack_is_full(self):
        my_stack = MyStack(3)
        my_stack.push(1)
        my_stack.push(2)
        my_stack.push(3)
        self.assertTrue(my_stack.is_full())

    def test_to_push_full_stack_is_not_possible(self):
        my_stack = MyStack(3)
        my_stack.push(1)
        my_stack.push(2)
        my_stack.push(3)
        with self.assertRaises(ValueError):
            my_stack.push(4)

    def test_pop_empty_stack(self):
        my_stack = MyStack(3)
        with self.assertRaises(ValueError):
            my_stack.pop()

import unittest
from stackdata import myqueue
from stackdata.myqueue import Queue


class TestQueue(unittest.TestCase):
    def test_that_app_enqueue_X_queue_is_not_empty(self):
        queue_test = Queue(4)
        given = queue_test.is_queue_empty()
        self.assertTrue(given)
        when = queue_test.enqueue("Abia")
        self.assertTrue(when)
        self.assertFalse(queue_test.is_queue_empty())

    def test_that_app_enqueueX_enqueue_Y_queue_is_not_empty(self):
        queue_test = Queue(4)
        given = queue_test.is_queue_empty()
        self.assertTrue(given)
        queue_test.enqueue("Abia")
        queue_test.enqueue("Adamawa")
        self.assertFalse(queue_test.is_queue_empty())

    def test_that_app_enqueueX_enqueueY_dequeue_Y_queue_is_not_empty(self):
        queue_test = Queue(4)
        given = queue_test.is_queue_empty()
        self.assertTrue(given)
        queue_test.enqueue("Abia")
        queue_test.enqueue("Adamawa")
        queue_test.enqueue("Akwa-Ibom")
        queue_test.enqueue("Anambra")
        self.assertFalse(queue_test.is_queue_empty())

    def test_that_app_enqueueX_enqueueY_dequeueX_queue_is_not_empty(self):
        queue_test = Queue(4)
        given = queue_test.is_queue_empty()
        self.assertTrue(given)
        queue_test.enqueue("Abia")
        queue_test.enqueue("Adamawa")

        queue_test.dequeue()
        self.assertFalse(queue_test.is_queue_empty())

    def test_that_app_can_enqueue_X_enqueue_Y_elements_is_2_dequeue_x_i_have_1_element_left_queue_is_not_empty(self):
        queue_test = Queue(4)
        given = queue_test.is_queue_empty()
        self.assertTrue(given)
        queue_test.enqueue("Abia")
        queue_test.enqueue("Adamawa")

        num_elements = queue_test.number_of_elements()
        self.assertEqual(num_elements, 2)
        queue_test.dequeue()
        self.assertFalse(queue_test.is_queue_empty())
        num_elements = queue_test.number_of_elements()
        self.assertEqual(num_elements, 1)

    def test_that_app_can_enqueue_X_dequeue_X_queue_is_now_empty(self):
        queue_test = Queue(4)
        given = queue_test.is_queue_empty()
        self.assertTrue(given)
        queue_test.enqueue("Abia")
        num_elements = queue_test.number_of_elements()
        self.assertEqual(num_elements, 1)
        queue_test.dequeue()
        self.assertTrue(queue_test.is_queue_empty())
        num_elements = queue_test.number_of_elements()
        self.assertEqual(num_elements, 0)




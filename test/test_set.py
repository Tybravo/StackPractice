import unittest

import stackdata.set
from stackdata.set import Set


class SetTest(unittest.TestCase):

    def setUp(self):
        self.my_set = set.Set()



    def test_that_set_add_items_to_the_set(self):
        self.my_set.add_element(1)
        self.assertIn(1, self.my_set.get_elements())
        self.my_set.add_element(2)
        self.assertIn(2, self.my_set.get_elements())
        self.assertEqual(self.my_set.get_size(), 2)


    def test_that_adding_duplicate_element_does_not_change_the_set(self):
        self.my_set.add_element("rice")
        self.my_set.add_element("beans")
        self.assertIn("rice", self.my_set.get_elements())
        self.assertIn("beans", self.my_set.get_elements())
        self.my_set.add_element("rice")
        self.assertEqual(self.my_set.get_size(), 2)


    def test_that_set_can_pop_items_from_the_set(self):
        self.my_set.add_element(25)
        self.my_set.add_element(33)
        self.assertEqual(self.my_set.get_size(), 2)
        self.my_set.pop_element(25)
        self.my_set.pop_element(33)
        self.assertEqual(self.my_set.get_size(), 0)



    def test_that_set_adds_3_items_and_pop2_size_returns_1(self):
        self.my_set.add_element(1)
        self.my_set.add_element(2)
        self.my_set.add_element(3)
        self.assertEqual(self.my_set.get_size(), 3)
        self.my_set.pop_element(3)
        self.my_set.pop_element(2)
        self.assertEqual(self.my_set.get_size(), 1)



    def test_popping_from_an_empty_set_raise_a_key_error(self):
        with self.assertRaises(KeyError):
            self.my_set.pop_element(1)
            self.my_set.pop_element(2)


    def test_that_set_can_be_updated_with_another_collection(self):
        self.my_set.add_element(10)
        self.my_set.add_element(20)
        self.my_set.add_element(30)
        self.my_set.update_set([40, 50, 60])
        self.assertIn(10, self.my_set.get_elements())
        self.assertIn(20, self.my_set.get_elements())
        self.assertIn(30, self.my_set.get_elements())
        self.assertIn(40, self.my_set.get_elements())
        self.assertIn(50, self.my_set.get_elements())
        self.assertIn(60, self.my_set.get_elements())
        self.assertEqual(self.my_set.get_size(), 6)



    def test_that_updating_set_duplicate_element_ensures_sets_always_unique(self):
        self.my_set.add_element("rice")
        self.my_set.add_element("beans")
        self.my_set.add_element("garri")
        self.my_set.update_set(["rice", "tea/bread", "yam"])
        self.assertIn("rice", self.my_set.get_elements())
        self.assertIn("beans", self.my_set.get_elements())
        self.assertIn("garri", self.my_set.get_elements())
        self.assertIn("yam", self.my_set.get_elements())
        self.assertIn("tea/bread", self.my_set.get_elements())
        self.assertEqual(self.my_set.get_size(), 5)


    def test_update_set_with_empty_iterable(self):
        self.my_set.add_element(1)
        self.my_set.add_element(2)
        self.my_set.update_set([])
        self.assertIn(1, self.my_set.get_elements())
        self.assertIn(2, self.my_set.get_elements())
        self.assertEqual(self.my_set.get_size(), 2)


    def test_that_set_can_add_3_items_and_clear_all(self):
        self.my_set.add_element(11)
        self.my_set.add_element(22)
        self.my_set.add_element(33)
        self.my_set.clear_all_elements()
        self.assertEqual(self.my_set.get_size(), 0)



    def test_that_remove_method_removes_items_from_the_set(self):
        self.my_set.add_element(11)
        self.my_set.add_element(22)
        self.my_set.remove_element(22)
        self.assertNotIn(22, self.my_set.get_elements())
        self.assertEqual(self.my_set.get_size(), 1)


    def test_for_removing_an_item_not_in_the_list(self):
        self.my_set.add_element(11)
        self.my_set.add_element(22)
        with self.assertRaises(KeyError):
            self.my_set.remove_element(20)


    def test_remove_from_empty_set(self):
        # Attempt to remove an element from an empty set
        with self.assertRaises(KeyError):
            self.my_set.remove_element(1)

    def test_discard_to_remove_element_found_in_the_set(self):
        self.my_set.add_element(11)
        self.my_set.add_element(22)
        self.assertEqual(self.my_set.get_size(),2)
        self.my_set.discard(22)
        self.assertNotIn(22, self.my_set.get_elements())
        self.assertEqual(self.my_set.get_size(),1)


    def test_discard_to_remove_element_not_found_in_the_set(self):
        self.my_set.add_element(11)
        self.my_set.add_element(22)
        self.my_set.discard(50)
        self.assertNotIn(50, self.my_set.get_elements())
        self.assertEqual(self.my_set.get_size(),2)


    def test_find_element_with_findMethod(self):
        self.my_set.add_element(10)
        self.my_set.add_element(22)
        self.assertEqual(self.my_set.find_element(10), 10)
        self.assertEqual(self.my_set.find_element(22), 22)



    def test_find_element_raise_key_error_for_non_existing_element(self):
        self.my_set.add_element(11)
        with self.assertRaises(KeyError):
            self.my_set.find_element(3)




if __name__ == '__main__':
    unittest.main()


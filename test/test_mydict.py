

import unittest

from stackdata.my_dict import MyDict


class TestDict(unittest.TestCase):
    def setUp(self):
        self.my_dict = MyDict()

    def test_that_key_pairs_can_be_set(self):
        self.my_dict.set(1, "girl")
        self.my_dict.set(2, "boy")
        self.assertEqual(self.my_dict.get_key(1), "girl")
        self.assertEqual(self.my_dict.get_dict_size(), 2)

    def test_that_key_pairs_can_be_set_and_gotten(self):
        self.my_dict.set(1, "girl")
        self.my_dict.set(2, "boy")
        self.assertEqual(self.my_dict.get_key(1), "girl")
        self.assertEqual(self.my_dict.get_key(2), "boy")
        self.assertEqual(self.my_dict.get_dict_size(), 2)

    def test_that_you_can_get_keys_by_values_set(self):
        self.my_dict.set(55, "score_student1")
        self.my_dict.set(75, "score_student2")
        self.assertEqual(self.my_dict.get_key_by_value("score_student1"), 55)


    def test_that_replacing_values_for_a_key_works(self):
        self.my_dict.set(2, "Orange")
        self.my_dict.set(2, "Banana")
        self.assertEqual(self.my_dict.get_key(2), "Banana", "replacing Orange for Banana")


    def test_that_popByKey_removes_key_and_value_from_dict(self):
        self.my_dict.set(1, "Apple")
        self.my_dict.set(2, "Orange")
        self.assertEqual(self.my_dict.get_dict_size(), 2)
        self.my_dict.pop_key(1)
        self.assertEqual(self.my_dict.get_dict_size(), 1)


    def test_that_popping_from_an_empty_dict_raises_error(self):
        with self.assertRaises(KeyError):
            self.my_dict.pop_item()


    def test_that_dict_contains_a_particular_key(self):
        self.my_dict.set(234, "Nigeria")
        self.my_dict.set(233, "Ghana")
        self.assertTrue(self.my_dict.contains(234))
        self.assertTrue(self.my_dict.contains(233))


    def test_that_dict_adds_inputs_and_clears_them_all(self):
        self.my_dict.set(234, "Nigeria")
        self.my_dict.set(233, "Ghana")
        self.my_dict.set(256, "Kenya")
        self.assertEqual(self.my_dict.clear(), 0)


    def test_that_pop_item_removes_last_inserted_item(self):
        self.my_dict.set(1, "first")
        self.my_dict.set(2, "second")
        last_item = self.my_dict.pop_item()
        self.assertEqual(last_item, (2, "second"))
        self.assertEqual(self.my_dict.get_dict_size(), 1)



    def test_that_all_keys_in_dict_can_be_viewed(self):
        self.my_dict.set(1, "first")
        self.my_dict.set(2, "second")
        self.my_dict.set(3, "third")
        self.assertEqual(self.my_dict.keys_view(), {1, 2, 3})


    def test_that_all_values_in_dict_can_be_viewed(self):
        self.my_dict.set(10, "Jay-jay")
        self.my_dict.set(7, "R7")
        self.my_dict.set(8, "Lamps")
        self.assertEqual(self.my_dict.values_view(), ["Jay-jay", "R7", "Lamps"])


    def test_That_all_items_in_dict_can_be_viewed(self):
        self.my_dict.set(1, "apple")
        self.my_dict.set(2, "banana")
        self.my_dict.set(3, "cherry")
        self.assertEqual(self.my_dict.items_view(), [(1, "apple"), (2, "banana"), (3, "cherry")])






if __name__ == '__main__':
    unittest.main()

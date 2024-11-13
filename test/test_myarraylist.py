import unittest

from stackdata import myarraylist

class TestMyArrayList(unittest.TestCase):
    def setUp(self):
        self.arr= myarraylist.MyArrayList()

    def test_that_myarraylist_app_exist(self):
        exist = myarraylist.MyArrayList
        self.assertTrue(exist)

    def test_that_app_can_add_1_item__to_arraylist(self):
        arr = myarraylist.MyArrayList()
        arr.my_add(0, "Berry")
        self.assertTrue(arr.get(0), "Berry")

    def test_that_app_can_add_more_than_1_item_to_arraylist(self):
        arr = myarraylist.MyArrayList()
        arr.my_add(0, "Berry")
        arr.my_add(1, "Orange")
        arr.my_add(2, "Pineapple")
        self.assertTrue(arr.get(0), "Berry")
        self.assertTrue(arr.get(1), "Orange")
        self.assertTrue(arr.get(2), "Pineapple")

    def test_that_app_can_get_the_size_of_item_in_arraylist(self):
        arr = myarraylist.MyArrayList()
        arr.my_add(0, "Berry")
        arr.my_add(1, "Orange")
        arr.my_add(2, "Pineapple")
        self.assertEqual(3, arr.get_size())

    def test_that_app_can_remove_1_item_remain_2_from_arraylist(self):
        arr = myarraylist.MyArrayList()
        arr.my_add(0, "Berry")
        arr.my_add(1, "Orange")
        arr.my_add(2, "Pineapple")
        arr.my_remove(1)
        self.assertTrue(arr.get(0), "Berry")
        self.assertTrue(arr.get(1), "Pineapple")
        self.assertEqual(2,arr.get_size())

    def test_that_app_has_invalid_index(self):
        arr = myarraylist.MyArrayList()
        arr.my_add(0, "Berry")
        with self.assertRaises(IndexError):
            arr.get(3)







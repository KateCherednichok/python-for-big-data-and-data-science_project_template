from app.io.input import input_from_file_build_in, input_from_file_by_pandas
import unittest
import pandas

class TestInput(unittest.TestCase):
    def test_input_from_file_build_in_file_not_exist(self):
        with self.assertRaises(FileNotFoundError):
            input_from_file_build_in('../../data/error.txt')


    def test_input_from_file_build_in_file_exist(self):
        result_of_function = input_from_file_build_in('../../data/test1.txt')
        self.assertIsInstance(result_of_function, str)


    def test_input_from_file_build_in_empty_file(self):
        result_of_function = input_from_file_build_in('../../data/test2.txt')
        self.assertTrue(len(result_of_function) == 0)


    def test_input_from_file_by_pandas_file_not_exist(self):
        with self.assertRaises(FileNotFoundError):
            input_from_file_by_pandas('../../data/error.csv')


    def test_input_from_file_by_pandas_file_empty_file(self):
        with self.assertRaises(pandas.errors.EmptyDataError):
            input_from_file_by_pandas('../../data/emptyTest.csv')


    def test_input_from_file_by_pandas_file_exist(self):
        result_of_function = input_from_file_by_pandas('../../data/test1.txt')
        self.assertIsInstance(result_of_function, str)
        self.assertTrue(len(result_of_function) > 0)

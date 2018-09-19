from os.path import abspath
import sys

sys.path.append(abspath('../'))
import unittest
from io import StringIO
from main import Interpreter

class InterpreterTests(unittest.TestCase):

    def setUp(self):
        self.interpreter = Interpreter('John')

    def test_do_extract_valid_option_not_provided(self):
        # Arrange
        expected = 'Valid options not provided. Use "help extract" command'
        sys.stdout = mystdout = StringIO()
        self.interpreter.do_extract(" ")

        # Act
        actual = mystdout.getvalue().split("\n")[0]

        # Assert
        error_message = "Expected {} \n but got {}".format(expected, actual)
        self.assertTrue(expected == actual, error_message)

    def test_do_extract_valid_indicator_not_provided(self):
        # Arrange
        expected = 'Please provide valid indicator'
        sys.stdout = mystdout = StringIO()
        self.interpreter.do_extract("-c -./")

        # Act
        actual = mystdout.getvalue().split("\n")[0]

        # Assert
        error_message = "Expected {} \n but got {}".format(expected, actual)
        self.assertTrue(expected == actual, error_message)

    def test_do_extract_file_data(self):
        # Arrange
        expected = 1
        self.interpreter.do_extract('-f -../main.py')

        # Act
        actual = len(self.interpreter.extracted_data)

        # Assert
        error_message = "Expected {} class data but got {}".format(expected, actual)
        self.assertTrue(expected == actual, error_message)

    def test_do_extract_folder_data(self):
        # Arrange
        expected = 10
        self.interpreter.do_extract('-d -../')

        # Act
        actual = len(self.interpreter.extracted_data)

        # Assert
        error_message = "Expected {} class data but got {}".format(expected, actual)
        self.assertTrue(expected == actual, error_message)

    def test_do_extract_not_a_file(self):
        # Arrange
        expected = 0
        self.interpreter.do_extract('-f -../')

        # Act
        actual = len(self.interpreter.extracted_data)

        # Assert
        error_message = "Expected {} class data but got {}".format(expected, actual)
        self.assertTrue(expected == actual, error_message)

    def test_do_extract_invalid_file(self):
        # Arrange
        expected = 0
        self.interpreter.do_extract('-f -../rawUml.txt')

        # Act
        actual = len(self.interpreter.extracted_data)

        # Assert
        error_message = "Expected {} class data but got {}".format(expected, actual)
        self.assertTrue(expected == actual, error_message)

    def test_do_extract_invalid_directory(self):
        # Arrange
        expected = 0
        self.interpreter.do_extract('-d -../main.py')

        # Act
        actual = len(self.interpreter.extracted_data)

        # Assert
        error_message = "Expected {} class data but got {}".format(expected, actual)
        self.assertTrue(expected == actual, error_message)


if __name__ == '__main__':
    unittest.main(verbosity=2)


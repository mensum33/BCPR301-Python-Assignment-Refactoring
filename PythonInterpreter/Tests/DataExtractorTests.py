from os.path import abspath
from sys import path

path.append(abspath('../'))
from DataExtractor import DataExtractor
from FileHandler.FileReader import FileReader
import unittest


class DataExtractorTests(unittest.TestCase):

    def test_get_association_relationship_of_Interpreter_class(self):
        # Arrange
        expected = 4
        extractor = DataExtractor(FileReader.read(abspath('../main.py')))

        # Act
        actual = len(extractor.association)

        # Assert
        error_message = "Expected {} but got {}".format(expected, actual)
        self.assertTrue(expected == actual, error_message)

    def test_get_association_relationship_of_DataExtractor_class(self):
        # Arrange
        expected = 0
        extractor = DataExtractor(FileReader.read(abspath('../DataExtractor.py')))

        # Act
        actual = len(extractor.association)

        # Assert
        error_message = "Expected {} but got {}".format(expected, actual)
        self.assertTrue(expected == actual, error_message)

    def test_get_instance_attribute_of_DataExtractor_class(self):
        # Arrange
        expected = 6
        extractor = DataExtractor(FileReader.read(abspath('../DataExtractor.py')))

        # Act
        actual = len(extractor.instance_attributes)

        # Assert
        error_message = "Expected {} but got {}".format(expected, actual)
        self.assertTrue(expected == actual, error_message)

    def test_get_instance_attribute_of_UmlClass_class(self):
        # Arrange
        expected = 0
        extractor = DataExtractor(FileReader.read(abspath('../UmlClass.py')))

        # Act
        actual = len(extractor.instance_attributes)

        # Assert
        error_message = "Expected {} but got {}".format(expected, actual)
        self.assertTrue(expected == actual, error_message)

    def test_get_instance_attribute_of_interpreter_class(self):
        # Arrange
        expected = 0
        extractor = DataExtractor(FileReader.read(abspath('../UmlClass.py')))

        # Act
        actual = len(extractor.instance_attributes)

        # Assert
        error_message = "Expected {} but got {}".format(expected, actual)
        self.assertTrue(expected == actual, error_message)


if __name__ == '__main__':
    unittest.main(verbosity=2)

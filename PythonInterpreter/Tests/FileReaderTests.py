from os.path import abspath
from sys import path

path.append(abspath('../'))
from FileHandler.FileReader import FileReader
import unittest


class FileReaderTests(unittest.TestCase):
    def test_read_from_file_valid_file(self):
        # Arrange
        expected = True
        file_path = '../../TestData/fileData/ValidClassData.py'
        file_data = FileReader.read_from_file(file_path)

        # Act
        actual = file_data.startswith("class HelloWorld")

        # Assert
        error_message = "Expected {} but got {}".format(expected, actual)
        self.assertTrue(expected == actual, error_message)

    def test_read_from_file_invalid_file(self):
        # Arrange
        expected = ""
        file_path = '../../TestData/fileData/Invalid.txt'

        # Act
        actual = FileReader.read_from_file(file_path)

        # Assert
        error_message = "Expected {} but got {}".format(expected, actual)
        self.assertTrue(expected == actual, error_message)

    def test_read_from_file_invalid_data(self):
        # Arrange
        expected = ""
        file_path = '../../TestData/folderData/invalid/3.py'

        # Act
        actual = FileReader.read_from_file(file_path)

        # Assert
        error_message = "Expected {} but got {}".format(expected, actual)
        self.assertTrue(expected == actual, error_message)

    def test_read_from_file_valid_file_unformatted(self):
        # Arrange
        expected = True
        file_path = '../../TestData/fileData/ValidClassDataUnFormatted.py'
        file_data = FileReader.read_from_file(file_path)

        # Act
        actual = file_data.startswith("class HelloWorld")

        # Assert
        error_message = "Expected {} but got {}".format(expected, actual)
        self.assertTrue(expected == actual, error_message)

    def test_read_from_file_with_multiple_classes_unformatted(self):
        # Arrange
        expected = ""
        file_path = '../../TestData/folderData/multipleClassUnformatted/multipleClassUnformatted.py'

        # Act
        actual = FileReader.read_from_file(file_path)

        # Assert
        error_message = "Expected {} but got {}".format(expected, actual)
        self.assertTrue(expected == actual, error_message)

    def test_read_from_file_with_multiple_classes_formatted(self):
        # Arrange
        expected = ""
        file_path = '../../TestData/folderData/multipleClassFormatted/multipleClassFormatted.py'

        # Act
        actual = FileReader.read_from_file(file_path)

        # Assert
        error_message = "Expected {} but got {}".format(expected, actual)
        self.assertTrue(expected == actual, error_message)

    def test_read_from_folder_with_valid_files(self):
        # Arrange
        expected = 3
        folder_path = '../../TestData/folderData/valid'

        # Act
        actual = len(FileReader.read_from_folder(folder_path))

        # Assert
        error_message = "Expected data for {} class but got data from {} class".format(expected, actual)
        self.assertTrue(expected == actual, error_message)

    def test_read_from_folder_with_invalid_files(self):
        # Arrange
        expected = 0
        folder_path = '../../TestData/folderData/invalid'

        # Act
        actual = len(FileReader.read_from_folder(folder_path))

        # Assert
        error_message = "Expected data for {} class but got data from {} class".format(expected, actual)
        self.assertTrue(expected == actual, error_message)

    def test_read_from_folder_with_multiple_classes_unformatted(self):
        # Arrange
        expected = 0
        folder_path = '../../TestData/folderData/multipleClassUnformatted'

        # Act
        actual = len(FileReader.read_from_folder(folder_path))

        # Assert
        error_message = "Expected data for {} class but got data from {} class".format(expected, actual)
        self.assertTrue(expected == actual, error_message)

    def test_read_from_folder_with_multiple_classes_formatted(self):
        # Arrange
        expected = 0
        folder_path = '../../TestData/folderData/multipleClassFormatted'

        # Act
        actual = len(FileReader.read_from_folder(folder_path))

        # Assert
        error_message = "Expected data for {} class but got data from {} class".format(expected, actual)
        self.assertTrue(expected == actual, error_message)


if __name__ == '__main__':
    unittest.main(verbosity=2)

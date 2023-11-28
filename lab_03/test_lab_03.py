import unittest
from student import Student
from studentList import StudentList
from fileManager import FileManager
from unittest import TestCase, mock

class TestFileManagerMethods(unittest.TestCase):

    def test_load_data(self):
        test_file = "test_file.csv"
        with open(test_file, "w") as file:
            file.write("name,phone,age,gender\nAnna,1234567890,25,woman")
        student_list = FileManager.load_data(test_file)
        self.assertEqual(len(student_list.students), 1)

    @mock.patch("builtins.input", side_effect=["Anna", "1234567890", "25", "woman"])
    def test_save_data(self, mock_input):
        test_file = "test_file.csv"
        student_list = StudentList()
        student_list.addNewElement()
        FileManager.save_data(test_file, student_list)
        with open(test_file, "r") as file:
            content = file.read()
            self.assertIn("Anna", content)

class TestStudentListMethods(unittest.TestCase):

    @mock.patch("builtins.input", side_effect=["Anna", "1234567890", "25", "woman"])
    def test_addNewElement(self, mock_input):
        student_list = StudentList()
        student_list.addNewElement()
        self.assertEqual(len(student_list.students), 1)
        self.assertEqual(student_list.students[0].name, "Anna")

    @mock.patch("builtins.input", return_value="Anna")
    def test_deleteElement(self, mock_input):
        student_list = StudentList()
        student_list.addNewElement()
        student_list.deleteElement()
        self.assertEqual(len(student_list.students), 0)

    @mock.patch("builtins.input", side_effect=["Anna", "Bob", "9876543210", "30", "man"])
    def test_updateElement(self, mock_input):
        student_list = StudentList()
        student_list.addNewElement()
        student_list.updateElement()
        self.assertEqual(student_list.students[0].name, "Bob")
if __name__ == '__main__':
    unittest.main()
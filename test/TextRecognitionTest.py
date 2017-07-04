import unittest
from unittest import mock
import TextRecognition


class MyTestCase(unittest.TestCase):
    @mock.patch('TextRecognition.pyocr.get_available_tools')
    def test_set_language_happy_path(self, mock_pyocr):
        mock_pyocr.return_value = MockTool()
        self.text_recognition = TextRecognition.TextRecognition()

        self.text_recognition.set_language('jss')
        self.assertEqual(1, mock_pyocr.call_count)
        self.assertEqual('jss', self.text_recognition.lang)

    @mock.patch('TextRecognition.pyocr.get_available_tools')
    @mock.patch('TextRecognition.PI')
    def test_recognize_file_happy_path(self, mock_image, mock_pyocr):
        mock_pyocr.return_value = MockTool()
        self.text_recognition = TextRecognition.TextRecognition()

        result = self.text_recognition.recognize_file('fake_file')
        self.assertEqual(1, mock_pyocr.call_count)
        self.assertEqual("This is a string", result)

class MockTool(object):
    def __init__(self):
        self.l = ['jss', 'boo']

    def get_available_languages(self):
        return self.l

    def image_to_string(self, file, lang='', builder=''):
        return "This is a string"

    def __getitem__(self, index):
        return self

    def __setitem__(self, index, value):
        self.l[index] = value

if __name__ == '__main__':
    unittest.main()

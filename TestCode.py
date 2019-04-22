import unittest
from ProductionCode import *

class AddFunctionTestCase(unittest.TestCase):
    def setUp(self):
        self.list_of_numbers = "1,2,3,1"
        self.invalid_input = [1,2,3,1]
        self.input_with_other_delimiter = ";1;2;3;1"
        self.input_with_negative_number = "1,2,3,-1"

    def testReturnIntValue(self):
        self.assertIsInstance(Add(self.list_of_numbers),int,
                              "Return Error: The result is not int value")

    def testValidateInputError(self):
        with self.assertRaises((AttributeError,TypeError)):
            Add(self.invalid_input)

    def testValidateCorrectSum(self):
        self.assertEqual(Add(self.list_of_numbers),7,
                         "Sum Error: The result of sum is incorrect")

    def testOptionallyDelimiter(self):
        self.assertEqual(Add(self.input_with_other_delimiter,";"), 7,
                         "Error: Delimiter is not yet implemented")

    def testValidateDismissNegativeNumbers(self):
        self.assertEqual(Add(self.input_with_negative_number),6,
                         "Error: negative numbers are not dismiss")
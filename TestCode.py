import unittest
from ProductionCode import *

class AddFunctionTestCase(unittest.TestCase):
    def setUp(self):
        self.list_of_numbers = "1,2,3,1"

    def testReturnIntValue(self):
        self.assertIsInstance(Add(self.list_of_numbers),int,
                              "Return Error: The result is not int value")

import unittest

from app import App

from fakes import *
class App_Spec(unittest.TestCase):

    def setUp(self):
        self.output = FakeConsoleOutput()
        self.input = FakeInput()

    def should_print_the_sum_of_arguments(self):
        app = App('1,2,3', self.output, self.input)
        self.assertEqual("The result is 6", self.output.output[0])

    def should_ask_for_new_input(self):
        app = App('1,2,3', self.output, self.input)
        self.input.input = "1,2"
        app.getNextUserInput()
        self.assertEqual("another input please", self.output.output[len(self.output.output)-2])
        
        
    
        
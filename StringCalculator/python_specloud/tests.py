import unittest

from fakes import *
from String_calculator import StringCalculator

class StringCalculatorSpec(unittest.TestCase):

    def setUp(self):
        self.sc = StringCalculator()

    def should_return_zero_with_empty_input(self):
        val = self.sc.add("")
        self.assertEqual(val, 0)

    def should_sum_two_numbers(self):
        val = self.sc.add("1,2")
        self.assertEqual(val, 3)
        
    def should_sum_any_amount_of_numbers(self):
        val = self.sc.add("1,2,3,4,5")
        self.assertEqual(val, 15)
        
    def should_handle_newlines_instead_of_commas(self):
        val = self.sc.add("1\n2\n3")
        self.assertEqual(val, 6)
    
    def should_handle_midex_newlines_and_commas(self):
        val = self.sc.add("1\n2,3")
        self.assertEqual(val, 6)
        
    def should_support_different_delimeters(self):
        val = self.sc.add("//[;]\n1;2;3")
        self.assertEqual(val, 6)
    
    def should_throw_exception_if_negative_numbers_in_input(self):
        with self.assertRaises(ValueError):
            val = self.sc.add("1,-2,3")
        
    def should_display_text_in_case_of_negative_number_exception(self):
        with self.assertRaises(ValueError) as ve:
            val = self.sc.add("1,-2,3")
        self.assertEqual("negatives not allowed -2",  str(ve.exception))
        
    def should_display_all_invalid_numbers_in_case_of_negative_number_exception(self):
        with self.assertRaises(ValueError) as ve:
            val = self.sc.add("1,-2,-33,5")
        self.assertEqual("negatives not allowed -2 -33",  str(ve.exception))

    def should_ignore_numbers_bigger_than_1000(self):
        val = self.sc.add("1,1001,2")
        self.assertEqual(val, 3)
        
    def should_support_long_delimeters(self):
        val = self.sc.add("//[xxx]\n1xxx2xxx3")
        self.assertEqual(val, 6)
    
    def should_support_long_multiple_delimeters(self):
        val = self.sc.add("//[xxx][;]\n1xxx2;3")
        self.assertEqual(val, 6)
    
    def should_handle_all_mixed_delims(self):
        val = self.sc.add("//[xxx][;]\n1xxx2;3,4\n5;6")
        self.assertEqual(val, 21)
        
    def should_print_result_to_console(self):
        o = FakeConsoleOutput()
        sc = StringCalculator(o)
        val = sc.add("1,2")
        self.assertEqual(o.output[0], "The result is 3")

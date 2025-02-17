from django.test import SimpleTestCase

from app import calc

# import unittest

class calculate_test(SimpleTestCase):
    def test_calculate_fucntion(self):
        a=10
        b=10
        res=calc.calculate(a,b)
        return self.assertEqual(res,20)
        # return self.assertEqual(res,21)   # this will give make our test failed because 10+10=20  != 21
        
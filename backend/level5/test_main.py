import unittest
from main import start
import json

class TestMain(unittest.TestCase):
    def test_normal_data(self):
        "We expect everything to go just fine so the output should be equal"

        start('data/input.json')

        with open('data/expected_output.json') as expected_output:
            self.expected_output = json.load(expected_output)
        with open('data/output.json') as output:
            self.output = json.load(output)
        
        self.assertEqual(self.expected_output, self.output)

    def test_wrong_date(self):
        "The program shouldn't crash with a wrong date"
        start('data/test/wrong_date.json')

    def test_wrong_date_format(self):
        "The program shouldn't crash with a wrong date format"
        start('data/test/wrong_date_format.json')

    def test_car_price_positive(self):
        "The program shouldn't crash with a wrong car price"
        start('data/test/car_negative_price.json')

    def test_car_does_not_exist(self):
        "The program shouldn't crash with a wrong car"
        start('data/test/car_does_not_exist.json')

    def test_wrong_path(self):
        with self.assertRaises(IOError):
            start('data/fake/path.json')

    def test_empty_file(self):
        with self.assertRaises(ValueError):
            start('data/test/empty_file.json')
    


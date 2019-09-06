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

import unittest
import numpy as np
from main import calculate_summary  # Assuming the function is named calculate_summary

class TestScoreSummary(unittest.TestCase):
    def test_calculate_summary(self):
        data = {
            'Math': [88, 92, 79, 85, 90],
            'Science': [95, 85, 91, 89, 92],
            'English': [78, 82, 88, 90, 84],
            'History': [70, 75, 80, 85, 77]
        }
        expected_summary = {
            'Math': {'average': 86.8, 'max': 92, 'min': 79},
            'Science': {'average': 90.4, 'max': 95, 'min': 85},
            'English': {'average': 84.4, 'max': 90, 'min': 78},
            'History': {'average': 77.4, 'max': 85, 'min': 70}
        }
        self.assertEqual(calculate_summary(data), expected_summary)

    def test_calculate_summary_empty_data(self):
        data = {}
        expected_summary = {}
        self.assertEqual(calculate_summary(data), expected_summary)

    def test_calculate_summary_single_subject(self):
        data = {
            'Math': [100, 90, 80, 70, 60]
        }
        expected_summary = {
            'Math': {'average': 80.0, 'max': 100, 'min': 60}
        }
        self.assertEqual(calculate_summary(data), expected_summary)

    def test_calculate_summary_same_scores(self):
        data = {
            'Math': [80, 80, 80, 80, 80],
            'Science': [90, 90, 90, 90, 90]
        }
        expected_summary = {
            'Math': {'average': 80.0, 'max': 80, 'min': 80},
            'Science': {'average': 90.0, 'max': 90, 'min': 90}
        }
        self.assertEqual(calculate_summary(data), expected_summary)

if __name__ == '__main__':
    unittest.main()

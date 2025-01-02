import unittest
import sys
import os

# Add the project root directory to the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import get_first_tweet

class TestTwitterAPI(unittest.TestCase):
    def test_get_first_tweet(self):
        # Replace with a valid Twitter handle for testing
        handle = 'elonmusk'
        result = get_first_tweet(handle)
        print(result)  # Print the result to see the tweet text
        self.assertNotIn("An error occurred", result)
        self.assertNotIn("User not found", result)
        self.assertNotIn("No tweets found", result)

if __name__ == '__main__':
    unittest.main()
# test_steppethyme.py
"""
Tests for SteppeThyme module.
"""

import unittest
from steppethyme import SteppeThyme

class TestSteppeThyme(unittest.TestCase):
    """Test cases for SteppeThyme class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SteppeThyme()
        self.assertIsInstance(instance, SteppeThyme)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SteppeThyme()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

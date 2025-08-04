# test_coreinterpreter.py
"""
Tests for CoreInterpreter module.
"""

import unittest
from coreinterpreter import CoreInterpreter

class TestCoreInterpreter(unittest.TestCase):
    """Test cases for CoreInterpreter class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CoreInterpreter()
        self.assertIsInstance(instance, CoreInterpreter)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CoreInterpreter()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

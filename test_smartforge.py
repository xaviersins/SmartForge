# test_smartforge.py
"""
Tests for SmartForge module.
"""

import unittest
from smartforge import SmartForge

class TestSmartForge(unittest.TestCase):
    """Test cases for SmartForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SmartForge()
        self.assertIsInstance(instance, SmartForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SmartForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

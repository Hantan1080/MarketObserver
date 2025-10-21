# test_marketobserver.py
"""
Tests for MarketObserver module.
"""

import unittest
from marketobserver import MarketObserver

class TestMarketObserver(unittest.TestCase):
    """Test cases for MarketObserver class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MarketObserver()
        self.assertIsInstance(instance, MarketObserver)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MarketObserver()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

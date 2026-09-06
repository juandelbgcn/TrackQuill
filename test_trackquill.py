# test_trackquill.py
"""
Tests for TrackQuill module.
"""

import unittest
from trackquill import TrackQuill

class TestTrackQuill(unittest.TestCase):
    """Test cases for TrackQuill class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TrackQuill()
        self.assertIsInstance(instance, TrackQuill)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TrackQuill()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""
Unit tests for the Amenity class.
"""
from tests.test_models.test_base_model import TestBaseModel
from models.amenity import Amenity


class TestAmenity(TestBaseModel):
    """Tests for Amenity class."""

    def __init__(self, *args, **kwargs):
        """Initialize test class."""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Test if the name attribute is of type str."""
        new = self.value()
        self.assertEqual(type(new.name), str)

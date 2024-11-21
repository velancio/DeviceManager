import pytest

from src.dwelling_manager import DwellingManager


@pytest.fixture
def dwelling_manager():
    """Fixture to create a fresh DwellingManager for each test"""
    return DwellingManager()


class TestDwellingManager:
    """Test class for DwellingManager"""

    def test_create_dwelling(self, dwelling_manager):
        """Test dwelling creation functionality"""
        dwelling = dwelling_manager.create_dwelling("dwelling_1")

        assert dwelling is not None
        assert dwelling.get_dwelling_id() == "dwelling_1"

    def test_list_multiple_dwelling(self, dwelling_manager):
        """
        Test listing multiple devices of different types
        """

        # Create multiple devices
        dwellings = [
            dwelling_manager.create_dwelling("dwelling_1"),
            dwelling_manager.create_dwelling("dwelling_2"),
            dwelling_manager.create_dwelling("dwelling_3"),
            dwelling_manager.create_dwelling("dwelling_4"),
        ]

        # Verify all devices are in the list
        listed_dwellings = dwelling_manager.list_dwellings()
        assert len(listed_dwellings) == 4
        assert set(listed_dwellings) == set(dwellings)

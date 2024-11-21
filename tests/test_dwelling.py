import pytest

from src.dwelling import Dwelling
from src.hub import Hub


@pytest.fixture
def dwelling():
    """Fixture to create a fresh DeviceManager for each test"""
    return Dwelling("dwelling_1")


@pytest.fixture
def hub():
    """Fixture to create a fresh DeviceManager for each test"""
    return Hub("hub_1")


class TestDwelling:
    """Test class for dwelling"""
    def test_dwelling_id(self, dwelling):
        """Test retrieving dwelling_id functionality"""
        assert dwelling.get_dwelling_id() == "dwelling_1"

    def test_get_hub_from_dwelling(self, dwelling, hub):
        """Test retrieving hub from dwelling functionality"""
        dwelling.install_hub(hub)
        assert dwelling.get_hub() == hub

    def test_set_occupancy(self, dwelling):
        """Test setting occupancy for dwelling functionality"""
        dwelling.set_occupancy()
        assert dwelling.get_is_occupied()

    def test_reset_occupancy(self, dwelling):
        """Test resetting occupancy for dwelling functionality"""
        dwelling.reset_occupancy()
        assert not dwelling.get_is_occupied()

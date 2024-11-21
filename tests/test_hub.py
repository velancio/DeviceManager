import pytest

from src.device import DeviceType
from src.device_manager import DeviceManager
from src.hub import Hub


@pytest.fixture
def hub():
    """Fixture to create a fresh DeviceManager for each test"""
    return Hub("hub_1")


@pytest.fixture
def device_manager():
    """Fixture to create a fresh DeviceManager for each test"""
    return DeviceManager()


class TestHub:
    """Tests for Hub class"""

    def test_hub_id(self, hub):
        """Test retrieving hub_id functionality"""
        assert hub.get_hub_id() == "hub_1"

    def test_add_device_hub(self, hub, device_manager):
        """Test adding device to a hub functionality"""
        switch = device_manager.create_device(
            DeviceType.SWITCH, "switch_1", "Living Room Light"
        )
        lock = device_manager.create_device(DeviceType.LOCK, "lock_1", "Front Door")

        hub.add_device(switch)
        hub.add_device(lock)

        assert len(hub.get_paired_devices()) == 2
        assert "switch_1" in hub.get_paired_devices().keys()
        assert "lock_1" in hub.get_paired_devices().keys()
        assert switch in hub.get_paired_devices().values()
        assert lock in hub.get_paired_devices().values()

    def test_remove_device_hub(self, hub, device_manager):
        """Test removing device from a hub functionality"""
        switch = device_manager.create_device(
            DeviceType.SWITCH, "switch_1", "Living Room Light"
        )
        lock = device_manager.create_device(DeviceType.LOCK, "lock_1", "Front Door")

        hub.add_device(switch)
        hub.add_device(lock)

        hub.remove_device("lock_1")

        assert len(hub.get_paired_devices()) == 1
        assert "switch_1" in hub.get_paired_devices().keys()
        assert "lock_1" not in hub.get_paired_devices().keys()
        assert switch in hub.get_paired_devices().values()
        assert lock not in hub.get_paired_devices().values()

    def test_list_devices_connected_to_hub(self, hub, device_manager):
        """
        Test listing device connected to a hub functionality
        """
        # Create multiple devices
        devices = [
            device_manager.create_device(
                DeviceType.SWITCH, "switch_1", "Living Room Light"
            ),
            device_manager.create_device(DeviceType.LOCK, "lock_1", "Front Door"),
            device_manager.create_device(
                DeviceType.DIMMER, "dimmer_1", "Bedroom Dimmer"
            ),
            device_manager.create_device(
                DeviceType.THERMOSTAT, "thermo_1", "Main Thermostat"
            ),
        ]

        for device in devices:
            hub.add_device(device)

        # Verify all devices are in the list
        listed_devices = hub.list_devices()
        assert len(listed_devices) == 4
        assert set(listed_devices) == set(devices)

    def test_get_paired_devices_connected_to_hub(self, hub, device_manager):
        """
        Test getting devices paired to a hub functionality
        """
        # Create multiple devices
        devices = [
            device_manager.create_device(
                DeviceType.SWITCH, "switch_1", "Living Room Light"
            ),
            device_manager.create_device(DeviceType.LOCK, "lock_1", "Front Door"),
            device_manager.create_device(
                DeviceType.DIMMER, "dimmer_1", "Bedroom Dimmer"
            ),
            device_manager.create_device(
                DeviceType.THERMOSTAT, "thermo_1", "Main Thermostat"
            ),
        ]

        for device in devices:
            hub.add_device(device)

        # Verify all devices are in the list
        paired_devices = hub.get_paired_devices()
        assert len(paired_devices) == 4
        assert "switch_1" in hub.get_paired_devices().keys()
        assert "lock_1" in hub.get_paired_devices().keys()
        assert "dimmer_1" in hub.get_paired_devices().keys()
        assert "thermo_1" in hub.get_paired_devices().keys()

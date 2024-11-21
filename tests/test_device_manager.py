import pytest

from src.device import DeviceType
from src.device_manager import DeviceManager


@pytest.fixture
def device_manager():
    """Fixture to create a fresh DeviceManager for each test"""
    return DeviceManager()


class TestDeviceManager:
    """Tests for the DeviceManager class"""

    def test_create_device(self, device_manager):
        """Test device creation functionality"""
        switch = device_manager.create_device(
            DeviceType.SWITCH, "switch_1", "Living Room Light"
        )

        assert switch is not None
        assert switch.get_device_id() == "switch_1"
        assert switch.get_name() == "Living Room Light"
        assert not switch.get_paired()

    def test_delete_device(self, device_manager):
        """Test device deletion"""
        switch = device_manager.create_device(
            DeviceType.SWITCH, "switch_1", "Living Room Light"
        )
        assert switch.get_device_id() == "switch_1"

        device_manager.delete_device(switch.get_device_id())
        assert len(device_manager.list_devices()) == 0

    def test_list_devices_multiple_devices(self, device_manager):
        """
        Test listing multiple devices of different types
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

        # Verify all devices are in the list
        listed_devices = device_manager.list_devices()
        assert len(listed_devices) == 4
        assert set(listed_devices) == set(devices)

    def test_list_devices_after_deletion(self, device_manager):
        """
        Test listing devices after deleting a device
        """

        # Create multiple devices
        device_manager.create_device(DeviceType.SWITCH, "switch_1", "Living Room Light")
        lock = device_manager.create_device(DeviceType.LOCK, "lock_1", "Front Door")

        # Delete one device
        device_manager.delete_device("switch_1")

        # Verify only the non-deleted device remains
        listed_devices = device_manager.list_devices()
        assert len(listed_devices) == 1
        assert listed_devices[0] == lock

    @pytest.mark.parametrize(
        "device_type",
        [DeviceType.SWITCH, DeviceType.LOCK, DeviceType.DIMMER, DeviceType.THERMOSTAT],
    )
    def test_list_devices_by_type(self, device_type, device_manager):
        """
        Parametrized test to verify device listing for each device type
        """
        # Create a device of the specified type
        device = device_manager.create_device(
            device_type,
            f"{device_type.value}_1",
            f"{device_type.value.capitalize()} Device",
        )

        # Verify the device is in the list
        listed_devices = device_manager.list_devices()
        assert len(listed_devices) == 1
        assert listed_devices[0] == device
        assert listed_devices[0].get_device_id() == f"{device_type.value}_1"

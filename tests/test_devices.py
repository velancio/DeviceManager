import pytest

from src.device import DeviceType
from src.device_manager import DeviceManager
from src.devices.lock import LockStateRepr
from src.devices.switch import SwitchStateRepr
from src.devices.thermostat import ThermostatStateRepr
from src.hub import Hub


@pytest.fixture
def device_manager():
    """Fixture to create a fresh DeviceManager for each test"""
    return DeviceManager()


@pytest.fixture
def hub():
    """Fixture to create a fresh DeviceManager for each test"""
    return Hub("hub_1")


class TestDevices:
    """Test class for devices"""

    def test_pair(self, device_manager, hub):
        """Test pair device to hub functionality"""
        switch = device_manager.create_device(
            DeviceType.SWITCH, "switch_1", "Living Room Light"
        )
        hub.add_device(switch)
        assert switch.get_paired()

    def test_unpair(self, device_manager, hub):
        """Test unpair device from hub functionality"""
        switch = device_manager.create_device(
            DeviceType.SWITCH, "switch_1", "Living Room Light"
        )
        hub.add_device(switch)
        hub.remove_device("switch_1")
        assert not switch.get_paired()

    def test_dimmer(self, device_manager, hub):
        """Test dimmer device functionality"""
        dimmer = device_manager.create_device(
            DeviceType.DIMMER, "dimmer_1", "Bedroom Dimmer"
        )

        # check for brightness update within the range
        dimmer.update_state(brightness=40)
        assert dimmer.get_state()["brightness"] == 40

        # check for brightness update above the range capped to 100
        dimmer.update_state(brightness=150)
        assert dimmer.get_state()["brightness"] == 100

        # check for brightness update below the range capped to 0
        dimmer.update_state(brightness=-20)
        assert dimmer.get_state()["brightness"] == 0

    def test_switch(self, device_manager, hub):
        """Test switch device functionality"""
        switch = device_manager.create_device(
            DeviceType.SWITCH, "switch_1", "Living Room Light"
        )

        switch.update_state()
        assert switch.get_state()["state"] == SwitchStateRepr.ON.name

        switch.update_state()
        assert switch.get_state()["state"] == SwitchStateRepr.OFF.name

    def test_lock(self, device_manager, hub):
        """Test lock device functionality"""
        lock = device_manager.create_device(DeviceType.LOCK, "lock_1", "Front Door")

        lock.update_state()
        assert lock.get_state()["is_locked"] == LockStateRepr.LOCKED.name

        lock.update_state()
        assert lock.get_state()["is_locked"] == LockStateRepr.UNLOCKED.name

        # lock.update_state(is_locked=False, pin_code="1234")
        # assert not lock.get_state()["is_locked"]
        # assert lock.get_state()["pin_code"] == "1234"

    def test_lock_with_correct_pincode(self, device_manager, hub):
        """Test lock device with correct pincode functionality"""
        lock = device_manager.create_device(
            DeviceType.LOCK, "lock_1", "Front Door", pin_code="1234"
        )

        lock.update_state()
        assert lock.get_state()["is_locked"] == LockStateRepr.LOCKED.name

        lock.update_state(pin_code="1234")
        assert lock.get_state()["is_locked"] == LockStateRepr.UNLOCKED.name

    def test_lock_with_incorrect_pincode(self, device_manager, hub):
        """Test lock device with incorrect pincode functionality"""
        lock = device_manager.create_device(
            DeviceType.LOCK, "lock_1", "Front Door", pin_code="1234"
        )

        lock.update_state()
        assert lock.get_state()["is_locked"] == LockStateRepr.LOCKED.name

        with pytest.raises(ValueError) as exc_info:
            lock.update_state(pin_code="134")
        assert str(exc_info.value) == "Incorrect PIN code"
        assert lock.get_state()["is_locked"] == LockStateRepr.LOCKED.name

    def test_thermostat(self, device_manager, hub):
        """Test thermostat device functionality"""
        thermo = device_manager.create_device(
            DeviceType.THERMOSTAT, "thermo_1", "Main Thermostat", temperature=62.5
        )

        thermo.update_state(mode=ThermostatStateRepr.HEAT)
        assert thermo.get_state()["mode"] == ThermostatStateRepr.HEAT.name
        assert thermo.get_state()["temperature"] == 62.5

        thermo.update_state(mode=ThermostatStateRepr.COOL, temperature=82.5)
        assert thermo.get_state()["mode"] == ThermostatStateRepr.COOL.name
        assert thermo.get_state()["temperature"] == 82.5

        thermo.update_state(mode=ThermostatStateRepr.OFF)
        assert thermo.get_state()["mode"] == ThermostatStateRepr.OFF.name
        assert thermo.get_state()["temperature"] == 82.5

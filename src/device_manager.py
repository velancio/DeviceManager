from typing import Dict, List

from src.device import Device, DeviceType
from src.devices.dimmer import Dimmer
from src.devices.lock import Lock
from src.devices.switch import Switch
from src.devices.thermostat import Thermostat


class DeviceManager:
    """Manages a collection of devices."""

    def __init__(self) -> None:
        """Initializes a device manager."""
        self._devices: Dict[str, Device] = {}

    def create_device(
        self, device_type: DeviceType, device_id: str, name: str, **kwargs
    ) -> Device:
        """Create a device and adds it to the collection."""
        device_classes = {
            DeviceType.SWITCH: Switch,
            DeviceType.DIMMER: Dimmer,
            DeviceType.LOCK: Lock,
            DeviceType.THERMOSTAT: Thermostat,
        }
        device = device_classes[device_type](device_id, name, **kwargs)
        self._devices[device_id] = device
        return device

    def delete_device(self, device_id: str) -> None:
        """Create a device from the collection."""
        if device_id in self._devices:
            del self._devices[device_id]

    def list_devices(self) -> List[Device]:
        """Lists all devices from the collection."""
        return list(self._devices.values())

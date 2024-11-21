from typing import Dict, List

from src.device import Device


class Hub:
    """Represents a hub."""
    def __init__(self, hub_id: str) -> None:
        """Initializes a hub."""
        self._hub_id = hub_id
        self._paired_devices: Dict[str, Device] = {}

    def add_device(self, device: Device) -> None:
        """Adds a device to the hub."""
        device.pair()
        self._paired_devices[device.get_device_id()] = device

    def remove_device(self, device_id: str) -> None:
        """Removes a device from the hub."""
        if device_id in self._paired_devices:
            self._paired_devices[device_id].unpair()
            del self._paired_devices[device_id]

    def list_devices(self) -> List[Device]:
        """Lists all devices from the hub."""
        return list(self._paired_devices.values())

    def get_paired_devices(self) -> Dict[str, Device]:
        """Gets all devices paired to the hub."""
        return self._paired_devices

    def get_hub_id(self) -> str:
        """Returns the hub ID."""
        return self._hub_id

    def __repr__(self):
        """Representation of the object"""
        return f"{self.get_hub_id()}"

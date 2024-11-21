from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, Any


class DeviceType(Enum):
    """Enumeration of possible device types."""
    SWITCH = "switch"  # Switch device type
    DIMMER = "dimmer"  # Dimmer device type
    LOCK = "lock"  # Lock device type
    THERMOSTAT = "thermostat"  # Thermostat device type


class Device(ABC):
    """Abstract base class for devices."""
    def __init__(self, device_id: str, name: str, **kwargs) -> None:
        """Initializes a device."""
        self._device_id = device_id  # Unique device ID
        self._name = name  # Device name
        self._is_paired = False  # Paired status

    @abstractmethod
    def update_state(self, **kwargs) -> None:
        """Updates the state of the device."""

    def get_state(self) -> Dict[str, Any]:
        """Returns the current state of the device."""
        state = {
            "device_id": self._device_id,  # Device ID
            "name": self._name,  # Device name
            "is_paired": self._is_paired  # Paired status
        }
        return state

    def get_device_id(self) -> str:
        """Returns the device ID."""
        return self._device_id

    def get_name(self) -> str:
        """Returns the device name."""
        return self._name

    def get_paired(self) -> bool:
        """Returns the paired status."""
        return self._is_paired

    def pair(self) -> None:
        """Pairs the device."""
        self._is_paired = True

    def unpair(self) -> None:
        """Unpairs the device."""
        self._is_paired = False

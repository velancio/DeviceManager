from enum import Enum
from typing import Dict, Any, Optional

from src.device import Device


class DimmerDefaults(Enum):
    """Default values for dimmer settings"""
    MIN_BRIGTHNESS = 0
    MAX_BRIGTHNESS = 100
    DEFAULT_BRIGTHNESS = 50


class Dimmer(Device):
    """Represents a dimmer device"""
    def __init__(self, device_id: str, name: str, brightness: int = DimmerDefaults.DEFAULT_BRIGTHNESS.value) -> None:
        """Initializes a dimmer device with a given ID, name, and brightness"""
        super().__init__(device_id, name)
        self._brightness = brightness

    def update_state(self, brightness: Optional[int] = None) -> None:
        """Updates the brightness of the dimmer device"""
        if brightness is None:
            return
        self._brightness = max(DimmerDefaults.MIN_BRIGTHNESS.value, min(brightness, DimmerDefaults.MAX_BRIGTHNESS.value))

    def get_state(self) -> Dict[str, Any]:
        """Returns the current state of the dimmer device"""
        state = super().get_state()
        state.update({'brightness': self._brightness})
        return state

    def __repr__(self):
        """Representation of the object"""
        return f"{self.get_device_id()} brightness is at {self._brightness}"

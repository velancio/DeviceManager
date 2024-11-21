from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, Any

from src.device import Device


class SwitchStateRepr(Enum):
    """Enumeration of possible switch states."""

    ON = "ON"
    OFF = "OFF"


class SwitchState(ABC):
    """Abstract base class for switch states."""

    @abstractmethod
    def toggle(self, switch: Device) -> None:
        """Toggles the switch state."""
        pass


class OnSwitch(SwitchState):
    """On state for the switch."""

    def toggle(self, switch: Device) -> None:
        """Toggles the switch to off state."""
        switch.state = OffSwitch()

    def __repr__(self):
        """Representation of the object"""
        return f"{SwitchStateRepr.ON.name}"


class OffSwitch(SwitchState):
    """Off state for the switch."""

    def toggle(self, switch: Device) -> None:
        """Toggles the switch to on state."""
        switch.state = OnSwitch()

    def __repr__(self):
        """Representation of the object"""
        return f"{SwitchStateRepr.OFF.name}"


class Switch(Device):
    """Implementation of a switch device."""

    def __init__(self, device_id: str, name: str) -> None:
        """Initializes a switch device."""
        super().__init__(device_id, name)
        self.state = OffSwitch()

    def update_state(self) -> None:
        """Updates the state of the switch."""
        self.state.toggle(self)

    def get_state(self) -> Dict[str, Any]:
        """Returns the current state of the switch."""
        state = super().get_state()
        state.update({"state": self.state.__repr__()})
        return state

    def __repr__(self):
        """Representation of the object"""
        return f"{self.get_device_id()} is {self.state.__repr__()}"

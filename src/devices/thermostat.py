from abc import abstractmethod, ABC
from enum import Enum
from typing import Dict, Any, Optional

from src.device import Device

class IThermostat(Device):
    """Interface for thermostat devices."""
    @abstractmethod
    def get_temperature(self) -> float:
        """Returns the current temperature of the thermostat."""
        pass


class ThermostatStateRepr(Enum):
    """Enumeration of possible thermostat states."""
    HEAT = 'HEAT'
    COOL = 'COOL'
    OFF = 'OFF'


class ThermostatState(ABC):
    """Abstract base class for thermostat states."""


class HeatMode(ThermostatState):
    """Heat mode for the thermostat."""
    def __repr__(self):
        """Representation of the object"""
        return f"{ThermostatStateRepr.HEAT.name}"


class CoolMode(ThermostatState):
    """Cool mode for the thermostat."""
    def __repr__(self):
        """Representation of the object"""
        return f"{ThermostatStateRepr.COOL.name}"


class OffMode(ThermostatState):
    """Off mode for the thermostat."""
    def __repr__(self):
        """Representation of the object"""
        return f"{ThermostatStateRepr.OFF.name}"


class Thermostat(IThermostat):
    """Implementation of a thermostat device."""
    def __init__(self, device_id: str, name: str, temperature: float = 72) -> None:
        """Initializes a thermostat device."""
        super().__init__(device_id, name)
        self._temperature = temperature
        self.state = OffMode()
        self._modes = {
            ThermostatStateRepr.HEAT: HeatMode(),
            ThermostatStateRepr.COOL: CoolMode(),
            ThermostatStateRepr.OFF: OffMode(),
        }

    def update_state(self, mode: Optional[ThermostatStateRepr] = None, temperature: Optional[float] = None) -> None:
        """Updates the state of the thermostat."""
        if temperature is not None:
            self._temperature = temperature

        if mode is not None:
            if mode in self._modes:
                print(f"go to mode {mode} from {self.state.__repr__()}")
                state = self._modes[mode]
                if state is not None:
                    self.state = state
                print(f"State changed to {self.state.__repr__()}")
            else:
                raise ValueError("Invalid mode")

    def get_state(self) -> Dict[str, Any]:
        """Returns the current state of the thermostat."""
        state = super().get_state()
        state.update({'temperature': self._temperature, 'mode': self.state.__repr__()})
        return state

    def get_temperature(self) -> float:
        """Returns the current temperature of the thermostat."""
        return self._temperature

    def __repr__(self):
        """Representation of the object"""
        return f"{self.get_device_id()} is in {self.state.__repr__()} mode at {self._temperature}F"

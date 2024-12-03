from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, Any, Optional

from src.device import Device, State


class ILock(Device):
    """Interface for lock devices."""

    def __init__(
            self, device_id: str, name: str, pin_code: Optional[str] = None
    ) -> None:
        """Initializes a lock device."""
        super().__init__(device_id, name)
        self.state: LockState = Unlocked()
        self._pin_code: Optional[str] = pin_code

    @abstractmethod
    def verify_pin_code(self, pin_code: str) -> bool:
        """Verifies the pin code for the lock."""

    @abstractmethod
    def is_pin_code(self) -> bool:
        """Checks if the lock has a pin code."""


class LockStateRepr(Enum):
    """Enumeration of possible lock states."""

    LOCKED = "LOCKED"  # Locked state representation
    UNLOCKED = "UNLOCKED"  # Unlocked state representation


class Lock(ILock):
    """Implementation of a lock device."""

    def update_state(self, pin_code: Optional[str] = None, **kwargs) -> None:
        """Updates the state of the lock."""
        self.state.toggle(self, pin_code)

    def get_state(self) -> Dict[str, Any]:
        """Returns the current state of the lock."""
        state = super().get_state()
        state.update(
            {
                "is_locked": self.state.__repr__(),
                "pin_code_set": self._pin_code is not None,
            }
        )
        return state

    def verify_pin_code(self, pin_code: str) -> bool:
        """Verifies the pin code for the lock."""
        return self._pin_code == pin_code

    def is_pin_code(self) -> bool:
        """Checks if the lock has a pin code."""
        return self._pin_code is not None

    def __repr__(self) -> str:
        """Returns a string representation of the object."""
        return f"{self.get_device_id()} is {self.state.__repr__()}"


class LockState(State):
    """Abstract base class for lock states."""

    @abstractmethod
    def toggle(self, lock: Lock, pin_code: Optional[str] = None) -> None:
        """Toggles the lock state."""


class Locked(LockState):
    """Locked state for the lock."""

    def toggle(self, lock: Lock, pin_code: Optional[str] = None) -> None:
        """Toggles the lock to unlocked state."""
        if lock.is_pin_code():
            if pin_code and lock.verify_pin_code(pin_code):
                lock.state = Unlocked()
            else:
                raise ValueError("Incorrect PIN code")
        else:
            lock.state = Unlocked()

    def __repr__(self) -> str:
        """Returns a string representation of the object."""
        return f"{LockStateRepr.LOCKED.name}"


class Unlocked(LockState):
    """Unlocked state for the lock."""

    def toggle(self, lock: Lock, pin_code: Optional[str] = None) -> None:
        """Toggles the lock to locked state."""
        lock.state = Locked()

    def __repr__(self) -> str:
        """Returns a string representation of the object."""
        return f"{LockStateRepr.UNLOCKED.name}"

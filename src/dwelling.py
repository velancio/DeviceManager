from src.hub import Hub


class Dwelling:
    """Represents a dwelling with devices."""

    def __init__(self, dwelling_id: str) -> None:
        """Initializes a dwelling."""
        self._dwelling_id = dwelling_id  # Unique dwelling ID
        self._is_occupied = False  # Dwelling occupancy status
        self._hub: Hub = None  # Hub associated with the dwelling

    def install_hub(self, hub: Hub) -> None:
        """Adds a hub to the dwelling."""
        self._hub = hub

    def set_occupancy(self) -> None:
        """Sets the dwelling as occupied."""
        self._is_occupied = True

    def reset_occupancy(self) -> None:
        """Sets the dwelling as vacant."""
        self._is_occupied = False

    def get_dwelling_id(self) -> str:
        """Returns the Unique dwelling ID."""
        return self._dwelling_id

    def get_hub(self) -> Hub:
        """Returns the hub associated with the dwelling."""
        return self._hub

    def get_is_occupied(self) -> bool:
        """Returns the occupancy status of the dwelling."""
        return self._is_occupied

    def __repr__(self):
        """Representation of the object"""
        return f"{self.get_dwelling_id()} is {self.get_is_occupied()} and {self.get_hub()} has been setup"

from typing import Dict, List

from src.dwelling import Dwelling


class DwellingManager:
    """Manages a collection of dwellings."""

    def __init__(self) -> None:
        """Initializes a dwelling collection."""
        self._dwellings: Dict[str, Dwelling] = {}

    def create_dwelling(self, dwelling_id: str) -> Dwelling:
        """Creates a dwelling and adds it to the collection."""
        dwelling = Dwelling(dwelling_id)
        self._dwellings[dwelling_id] = dwelling
        return dwelling

    def list_dwellings(self) -> List[Dwelling]:
        """Lists all dwellings from the collection."""
        return list(self._dwellings.values())

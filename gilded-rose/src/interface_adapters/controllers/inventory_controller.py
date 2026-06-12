from __future__ import annotations

from application.update_inventory import UpdateInventoryUseCase


class InventoryController:
    def __init__(self, items):
        self.items = items
        self.use_case = UpdateInventoryUseCase()

    def update_quality(self) -> None:
        self.use_case.execute(self.items)

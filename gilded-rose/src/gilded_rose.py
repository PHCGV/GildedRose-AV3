from __future__ import annotations

from interface_adapters.controllers.inventory_controller import InventoryController


class GildedRose(object):
    def __init__(self, items):
        self.items = items
        self.controller = InventoryController(self.items)

    def update_quality(self):
        self.controller.update_quality()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

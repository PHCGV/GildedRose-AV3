from __future__ import annotations

from dataclasses import dataclass

from .quality_rules import LEGENDARY_QUALITY, decrease_quality, increase_quality


@dataclass
class ItemRule:
    def update(self, item) -> None:
        self.update_quality(item)
        self.update_sell_in(item)
        self.update_expired_quality(item)

    def update_quality(self, item) -> None:
        raise NotImplementedError

    def update_sell_in(self, item) -> None:
        item.sell_in -= 1

    def update_expired_quality(self, item) -> None:
        if item.sell_in < 0:
            self.handle_expired_item(item)

    def handle_expired_item(self, item) -> None:
        raise NotImplementedError


class NormalItemRule(ItemRule):
    def update_quality(self, item) -> None:
        decrease_quality(item, 1)

    def handle_expired_item(self, item) -> None:
        decrease_quality(item, 1)


class AgedBrieRule(ItemRule):
    def update_quality(self, item) -> None:
        increase_quality(item, 1)

    def handle_expired_item(self, item) -> None:
        increase_quality(item, 1)


class BackstagePassRule(ItemRule):
    def update_quality(self, item) -> None:
        increase_quality(item, 1)
        if item.sell_in <= 10:
            increase_quality(item, 1)
        if item.sell_in <= 5:
            increase_quality(item, 1)

    def handle_expired_item(self, item) -> None:
        item.quality = 0


class SulfurasRule(ItemRule):
    def update(self, item) -> None:
        item.quality = LEGENDARY_QUALITY

    def update_quality(self, item) -> None:
        item.quality = LEGENDARY_QUALITY

    def update_sell_in(self, item) -> None:
        return

    def handle_expired_item(self, item) -> None:
        return


class ConjuredItemRule(ItemRule):
    def update_quality(self, item) -> None:
        decrease_quality(item, 2)

    def handle_expired_item(self, item) -> None:
        decrease_quality(item, 2)

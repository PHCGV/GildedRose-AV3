from __future__ import annotations


MAX_QUALITY = 50
MIN_QUALITY = 0
LEGENDARY_QUALITY = 80


def increase_quality(item, amount: int = 1) -> None:
    item.quality = min(MAX_QUALITY, item.quality + amount)


def decrease_quality(item, amount: int = 1) -> None:
    item.quality = max(MIN_QUALITY, item.quality - amount)

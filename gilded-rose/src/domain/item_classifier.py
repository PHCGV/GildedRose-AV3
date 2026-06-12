from __future__ import annotations

from .constants import AGED_BRIE, BACKSTAGE_PASSES, CONJURED_PREFIX, SULFURAS
from .item_rules import (
    AgedBrieRule,
    BackstagePassRule,
    ConjuredItemRule,
    NormalItemRule,
    SulfurasRule,
)


def get_rule_for(item_name: str):
    if item_name == AGED_BRIE:
        return AgedBrieRule()
    if item_name == BACKSTAGE_PASSES:
        return BackstagePassRule()
    if item_name == SULFURAS:
        return SulfurasRule()
    if item_name.startswith(CONJURED_PREFIX):
        return ConjuredItemRule()
    return NormalItemRule()

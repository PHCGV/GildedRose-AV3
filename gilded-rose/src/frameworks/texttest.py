from __future__ import annotations

from gilded_rose import GildedRose, Item
from interface_adapters.presenters.report_presenter import present_inventory_day


def build_default_items() -> list[Item]:
    return [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
        Item(name="Conjured Mana Cake", sell_in=3, quality=6),
    ]


def render_inventory_report(days: int) -> str:
    lines = ["OMGHAI!"]
    items = build_default_items()

    for day in range(days + 1):
        lines.append(present_inventory_day(day, items))
        lines.append("")
        GildedRose(items).update_quality()

    return "\n".join(lines) + "\n"

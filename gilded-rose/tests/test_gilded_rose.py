from __future__ import annotations

from pathlib import Path

from application.update_inventory import UpdateInventoryUseCase
from gilded_rose import GildedRose, Item
from interface_adapters.presenters.report_presenter import present_inventory_day
from texttest_fixture import render_inventory_report


def update_once(name: str, sell_in: int, quality: int) -> Item:
    item = Item(name, sell_in, quality)
    GildedRose([item]).update_quality()
    return item


def test_common_item_decreases_by_one_before_sell_date() -> None:
    item = update_once("+5 Dexterity Vest", 10, 20)

    assert item.sell_in == 9
    assert item.quality == 19


def test_common_item_decreases_twice_as_fast_after_sell_date() -> None:
    item = update_once("+5 Dexterity Vest", 0, 20)

    assert item.sell_in == -1
    assert item.quality == 18


def test_common_item_quality_never_becomes_negative() -> None:
    item = update_once("+5 Dexterity Vest", 0, 0)

    assert item.sell_in == -1
    assert item.quality == 0


def test_aged_brie_increases_in_quality() -> None:
    item = update_once("Aged Brie", 2, 0)

    assert item.sell_in == 1
    assert item.quality == 1


def test_aged_brie_increases_twice_as_fast_after_sell_date() -> None:
    item = update_once("Aged Brie", 0, 48)

    assert item.sell_in == -1
    assert item.quality == 50


def test_sulfuras_never_changes() -> None:
    item = update_once("Sulfuras, Hand of Ragnaros", 0, 80)

    assert item.sell_in == 0
    assert item.quality == 80


def test_backstage_passes_increase_by_one_when_sell_in_is_above_ten() -> None:
    item = update_once("Backstage passes to a TAFKAL80ETC concert", 15, 20)

    assert item.sell_in == 14
    assert item.quality == 21


def test_backstage_passes_increase_by_two_when_ten_days_or_less_remain() -> None:
    item = update_once("Backstage passes to a TAFKAL80ETC concert", 10, 20)

    assert item.sell_in == 9
    assert item.quality == 22


def test_backstage_passes_increase_by_three_when_five_days_or_less_remain() -> None:
    item = update_once("Backstage passes to a TAFKAL80ETC concert", 5, 20)

    assert item.sell_in == 4
    assert item.quality == 23


def test_backstage_passes_drop_to_zero_after_concert() -> None:
    item = update_once("Backstage passes to a TAFKAL80ETC concert", 0, 20)

    assert item.sell_in == -1
    assert item.quality == 0


def test_conjured_items_decrease_twice_as_fast_as_common_items() -> None:
    item = update_once("Conjured Mana Cake", 3, 6)

    assert item.sell_in == 2
    assert item.quality == 4


def test_conjured_items_decrease_four_points_after_sell_date() -> None:
    item = update_once("Conjured Mana Cake", 0, 6)

    assert item.sell_in == -1
    assert item.quality == 2


def test_update_inventory_use_case_updates_items_through_application_layer() -> None:
    item = Item("+5 Dexterity Vest", 10, 20)

    UpdateInventoryUseCase().execute([item])

    assert item.sell_in == 9
    assert item.quality == 19


def test_report_presenter_formats_inventory_day_output() -> None:
    items = [Item("+5 Dexterity Vest", 10, 20), Item("Aged Brie", 2, 0)]

    report = present_inventory_day(0, items)

    assert report == "\n".join(
        [
            "-------- day 0 --------",
            "name, sellIn, quality",
            "+5 Dexterity Vest, 10, 20",
            "Aged Brie, 2, 0",
        ]
    )


def test_fixture_output_matches_expected_snapshot_for_two_days() -> None:
    expected = (
        Path(__file__).parent / "snapshots" / "expected_inventory_report_2_days.txt"
    ).read_text(encoding="utf-8")

    assert render_inventory_report(2) == expected

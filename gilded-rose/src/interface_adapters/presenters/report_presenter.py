from __future__ import annotations

def present_inventory_day(day: int, items) -> str:
    lines = [f"-------- day {day} --------", "name, sellIn, quality"]
    lines.extend(str(item) for item in items)
    return "\n".join(lines)

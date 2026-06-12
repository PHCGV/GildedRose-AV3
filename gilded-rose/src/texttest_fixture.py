from __future__ import annotations

from frameworks.texttest import build_default_items, render_inventory_report


def main() -> None:
    import sys

    days = 2
    if len(sys.argv) > 1:
        days = int(sys.argv[1])

    print(render_inventory_report(days), end="")


if __name__ == "__main__":
    main()

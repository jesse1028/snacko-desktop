"""Snacko Desktop — A local helper for Snacko island folders, shop files, and cat-cafe photos."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='snacko_desktop',
        description='A local helper for Snacko island folders, shop files, and cat-cafe photos.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Snacko Desktop')
    print('Keep the snack island on disk before a market patch.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

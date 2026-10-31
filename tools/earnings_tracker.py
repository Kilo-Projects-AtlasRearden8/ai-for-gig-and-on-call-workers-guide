#!/usr/bin/env python3
"""Local earnings tracker for gig and on-call work.

Logs payments to earnings.csv (CSV) in the current folder. Nothing is uploaded.
Amounts are plain numbers (e.g. 180.00).
"""

import csv
import os
import sys
from datetime import datetime

DATA_FILE = "earnings.csv"
FIELDS = ["date", "source", "amount", "notes"]


def load_rows():
    rows = []
    if not os.path.exists(DATA_FILE):
        return rows
    with open(DATA_FILE, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            rows.append(row)
    return rows


def save_rows(rows):
    with open(DATA_FILE, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def cmd_add(args):
    if len(args) < 3:
        print("Usage: earnings_tracker.py add DATE SOURCE AMOUNT [NOTES]")
        return 1
    date, source, amount = args[0], args[1], args[2]
    notes = args[3] if len(args) > 3 else ""

    # Validate inputs before touching the file.
    try:
        datetime.strptime(date, "%Y-%m-%d")
        float(amount)  # validate
    except ValueError:
        print("Invalid input. Use: add DATE SOURCE AMOUNT [NOTES]")
        print('Example: add 2026-10-02 "rideshare app" 180.00')
        return 1
    rows = load_rows()
    rows.append({"date": date, "source": source, "amount": amount, "notes": notes})
    save_rows(rows)
    print(f"Added {date}: {source} ${amount}")
    return 0


def cmd_list(args):
    rows = load_rows()
    if not rows:
        print("No earnings logged yet.")
        return 0
    print(f"{'Date':<11} {'Source':<24} {'Amount':>10}  Notes")
    for r in rows:
        print(f"{r['date']:<11} {r['source']:<24} ${r['amount']:>9}  {r['notes']}")
    return 0


def cmd_total(args):
    rows = load_rows()
    month = None
    if args and args[0] == "--month" and len(args) > 1:
        month = args[1]
    total = 0.0
    count = 0
    for r in rows:
        if month and not r["date"].startswith(month):
            continue
        total += float(r["amount"])
        count += 1
    label = month if month else "all logged payments"
    print(f"{label}: {count} payment(s), ${total:.2f}")
    return 0


COMMANDS = {
    "add": cmd_add,
    "list": cmd_list,
    "total": cmd_total,
}


def main(argv):
    args = list(argv)
    if args and args[0] in COMMANDS:
        name, rest = args[0], args[1:]
    elif len(args) >= 2 and args[1] in COMMANDS:
        name, rest = args[1], args[2:]
    else:
        print("Usage: earnings_tracker.py <add|list|total> ...")
        print("Example: earnings_tracker.py add 2026-10-02 \"rideshare app\" 180.00")
        return 1
    return COMMANDS[name](rest)


if __name__ == "__main__":
    sys.exit(main(sys.argv))

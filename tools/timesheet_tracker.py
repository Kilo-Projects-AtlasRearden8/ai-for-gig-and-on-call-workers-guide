#!/usr/bin/env python3
"""Local timesheet tracker for irregular schedules.

Logs shifts to shifts.csv (CSV) in the current folder. Nothing is uploaded.
Times are 24-hour (HH:MM). Overnight shifts are handled automatically.
"""

import csv
import os
import sys
from datetime import datetime, timedelta

DATA_FILE = "shifts.csv"
FIELDS = ["date", "start", "end", "breaks_min", "rate", "hours", "total"]


def parse_time(value):
    return datetime.strptime(value, "%H:%M")


def shift_hours(start, end):
    s = parse_time(start)
    e = parse_time(end)
    if e <= s:
        e += timedelta(days=1)  # overnight shift
    return (e - s).total_seconds() / 3600.0


def load_shifts():
    shifts = []
    if not os.path.exists(DATA_FILE):
        return shifts
    with open(DATA_FILE, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            shifts.append(row)
    return shifts


def save_shifts(shifts):
    with open(DATA_FILE, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS)
        writer.writeheader()
        for row in shifts:
            writer.writerow(row)


def cmd_add(args):
    if len(args) < 4:
        print("Usage: timesheet_tracker.py add DATE START END [BREAKS_MIN] [RATE]")
        return 1
    date, start, end = args[0], args[1], args[2]
    breaks = args[3] if len(args) > 3 else "0"
    rate = args[4] if len(args) > 4 else "0"

    # Validate inputs before touching the file.
    try:
        datetime.strptime(date, "%Y-%m-%d")
        parse_time(start)
        parse_time(end)
        int(breaks)
        float(rate)
    except ValueError:
        print("Invalid input. Use: add DATE START END [BREAKS_MIN] [RATE]")
        print("Example: add 2026-10-01 07:00 19:00 30 22.50")
        return 1

    hours = round(shift_hours(start, end) - int(breaks) / 60.0, 2)
    total = round(hours * float(rate), 2)

    shifts = load_shifts()
    shifts.append(
        {
            "date": date,
            "start": start,
            "end": end,
            "breaks_min": breaks,
            "rate": rate,
            "hours": hours,
            "total": total,
        }
    )
    save_shifts(shifts)
    print(f"Added {date}: {hours} hours x ${rate} = ${total}")
    return 0


def cmd_list(args):
    shifts = load_shifts()
    if not shifts:
        print("No shifts logged yet.")
        return 0
    print(f"{'Date':<11} {'Start':<7} {'End':<6} {'Hrs':>5} {'Rate':>7} {'Total':>8}")
    for s in shifts:
        print(
            f"{s['date']:<11} {s['start']:<7} {s['end']:<6} "
            f"{s['hours']:>5} ${s['rate']:>6} ${s['total']:>7}"
        )
    return 0


def cmd_total(args):
    shifts = load_shifts()
    month = None
    if args and args[0] == "--month" and len(args) > 1:
        month = args[1]
    total_hours = 0.0
    total_pay = 0.0
    for s in shifts:
        if month and not s["date"].startswith(month):
            continue
        total_hours += float(s["hours"])
        total_pay += float(s["total"])
    label = month if month else "all logged shifts"
    print(f"{label}: {total_hours:.2f} hours, ${total_pay:.2f}")
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
        print("Usage: timesheet_tracker.py <add|list|total> ...")
        print("Example: timesheet_tracker.py add 2026-10-01 07:00 19:00 30 22.50")
        return 1
    return COMMANDS[name](rest)


if __name__ == "__main__":
    sys.exit(main(sys.argv))

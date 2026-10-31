# tools/

Small, local-first helper scripts for gig, on-call, and irregular-schedule
workers. Every script:

- runs on your own computer,
- saves data only to files on your computer,
- needs no API keys, no accounts, and no internet.

## Scripts

- `timesheet_tracker.py` — log shifts and total hours/pay.
- `earnings_tracker.py` — record payments and summarize by month.
- `shift_swap_helper.py` — draft a polite shift-swap message.

## Data files

Each script keeps a small CSV file in the folder where you run it:

- `shifts.csv`
- `earnings.csv`

You can copy, back up, print, or delete these files at any time. Nothing is
ever uploaded.

## Requirements

Python 3 only. No extra packages.

## Example

    python3 tools/timesheet_tracker.py add 2026-10-01 07:00 19:00 30 22.50
    python3 tools/timesheet_tracker.py total
    python3 tools/earnings_tracker.py add 2026-10-02 "rideshare app" 180.00
    python3 tools/earnings_tracker.py total --month 2026-10

Times in 24-hour format. Overnight shifts (start after end) are handled
automatically.

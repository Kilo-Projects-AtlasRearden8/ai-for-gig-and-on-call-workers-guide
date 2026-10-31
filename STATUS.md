# STATUS — AI for Gig, On-Call, and Irregular-Schedule Workers

## What was built

A beginner manual and static site for workers with unpredictable hours
(gig, on-call, shift, freelance), published by **Asdale Dynamics, LLC**.

- `docs/` — beginner manual in plain English:
  - `index.md` — overview and who this is for
  - `02-ai-basics.md` — AI/LLM/prompt/agent/MCP in plain English
  - `03-timesheets-earnings.md` — logging shifts, AI cleanup of notes,
    weekly review, printable worksheets
  - `04-shift-swaps.md` — swap rules, what to include, AI draft example,
    swap log, pay-rate warning
  - `05-simple-automation.md` — small local-first automations, one-at-a-time
    rule, helper scripts
  - `06-local-ai-privacy.md` — Ollama/LM Studio, privacy rules of thumb,
    education-only note for healthcare workers
  - `07-resources.md` — Asdale Dynamics, LLC credit and next steps
- `static/` — small HTML site (open any page in a browser):
  - `index.html`, `timesheet.html`, `earnings.html`, `shiftswap.html`,
    `automation.html`, plus shared `styles.css` and `script.js`
  - `timesheet.html` logs shifts client-side and prints a clean sheet
  - `earnings.html` tracks payments across sources
  - `shiftswap.html` drafts a polite swap message (nothing leaves the browser)
  - `automation.html` includes a client-side weekly earnings adder
- `worksheets/` — printable, print-ready HTML worksheets:
  - `timesheet-worksheet.html` (one week per page)
  - `earnings-worksheet.html` (monthly summary + paystub comparison)
  - `shift-swap-worksheet.html` (swap log with approval/pay checkboxes)
- `tools/` — local-first Python scripts (no API keys, no accounts, no uploads):
  - `timesheet_tracker.py` — add/list/total shifts to `shifts.csv`
  - `earnings_tracker.py` — add/list/total payments to `earnings.csv`
  - `shift_swap_helper.py` — prints a swap-message draft to stdout
  - `README.md`
- `tests/` — unittest/pytest tests for all three tools (13 tests, all pass)
- `LICENSE` — MIT License, copyright line exactly
  `Copyright (c) 2026 Asdale Dynamics, LLC`
- `README.md` — credits Dylan Asdale and Asdale Dynamics, LLC
- `.gitignore` — keeps personal data files (`shifts.csv`, `earnings.csv`)
  out of git

## How to run it

**Static site:** open `static/index.html` (or any `static/*.html` / `worksheets/*.html`)
in a web browser. No build step, no internet required once downloaded.

**Print worksheets:** open a `worksheets/*.html` file and use the browser's
Print command (print styles hide navigation and buttons).

**Helper scripts:**
```
python3 tools/timesheet_tracker.py add 2026-10-01 07:00 15:00 30 22.50
python3 tools/timesheet_tracker.py total
python3 tools/earnings_tracker.py add 2026-10-02 "rideshare app" 180.00
python3 tools/earnings_tracker.py total --month 2026-10
python3 tools/shift_swap_helper.py "Jordan" 2026-10-04 19:00 07:00 \
  "family commitment" "I can cover one of your future shifts"
```
Python 3 only, no extra packages. Data stays in CSV files on your computer.

**Tests:**
```
python3 -m pytest tests/
```
or `python3 -m unittest discover -s tests -v` if pytest is unavailable.

## Verification results

- `python3 -m pytest tests/` — **13 passed**
- Manual end-to-end runs of all three scripts — shift logging (including
  overnight shifts), earnings totals by month, and swap-message draft all work
- HTML tag balance validated for all 8 HTML files — OK
- No `.github/workflows` files present
- No secrets, API keys, or personal data in any committed file
- LICENSE copyright line verified exactly:
  `Copyright (c) 2026 Asdale Dynamics, LLC`
- README credits Asdale Dynamics, LLC

## Known gaps

- Worksheets are printable HTML but not pre-rendered PDFs (print from browser
  to PDF if needed).
- The site is static HTML with client-side JavaScript only; data entered in
  the browser is not saved between sessions (use `tools/` scripts or the
  printable worksheets for durable records).
- No PDF generation, no cloud sync, no accounts — by design (local-first).
- Healthcare content is education only, not medical advice.
- Not yet registered with PyPI or published anywhere; no remote repo created.

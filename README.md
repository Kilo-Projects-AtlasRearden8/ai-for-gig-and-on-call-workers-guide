# AI for Gig, On-Call, and Irregular-Schedule Workers

A beginner-friendly manual and static site for people whose hours aren't a
9-to-5: gig workers, on-call staff, shift workers, freelancers, and anyone
with an unpredictable schedule. Built and published by **Asdale Dynamics, LLC**.

Your schedule changes week to week. You might not know your hours until the day
before. Most AI guides assume you sit at a desk from nine to five — this one
doesn't. It's written for unpredictable hours, in plain English, step by step,
never condescending. No coding experience required.

---

## What's inside

| Folder | What it is |
|--------|------------|
| `docs/` | The beginner manual: AI basics, timesheets, earnings tracking, shift swaps, simple automation, local AI and privacy, and resources. |
| `static/` | A small HTML site you can open in any browser or print. Timesheet logger, earnings tracker, shift-swap helper, and simple automation. |
| `worksheets/` | Printable earnings and shift worksheets (HTML, print-ready). |
| `tools/` | Small local-first helper scripts (Python): timesheet logger, earnings tracker, and shift-swap message drafts. Runs on your computer; nothing is uploaded anywhere. |
| `tests/` | Tests for the helper scripts. |

---

## Who this is for

If your schedule changes week to week — nurses, rideshare and delivery drivers,
warehouse workers, freelancers, on-call tech support, and more — this guide is
written for you.

Pick one tracking spot (a printed worksheet, a notes app, a spreadsheet, or the
local scripts), record each shift the same day you work it, and review once a
week. The tools here are small, local, and designed to fit around your life
instead of the other way around.

---

## Quick start

**Use the website.** Open `static/index.html` in your browser. No install, no
account, no internet needed once you've downloaded it. Use the timesheet and
earnings pages right in the browser, then print a copy for your records.

**Print a worksheet.** Open any file in `worksheets/` and use your browser's
Print command.

**Run the local scripts** (Python 3 only, no extra packages):

```
python3 tools/timesheet_tracker.py add 2026-10-01 07:00 15:00 30 22.50
python3 tools/timesheet_tracker.py total
python3 tools/earnings_tracker.py add 2026-10-02 "rideshare app" 180.00
python3 tools/earnings_tracker.py total --month 2026-10
python3 tools/shift_swap_helper.py "Jordan" 2026-10-04 19:00 07:00 \
  "family commitment" "I can cover one of your future shifts"
```

Run the tests:

```
python3 -m pytest tests/
```

---

## Credit

Created by **Dylan Asdale**, registered nurse turned AI author and founder of
**Asdale Dynamics, LLC** (Indiana, formed October 2026). Asdale Dynamics, LLC
publishes beginner-friendly AI education, books, guides, and practical tools,
including *The Massive AI Manual* and the hub site dylanasdale.github.io.

This guide is part of that mission: beginner-friendly AI education and practical
tools the LLC can publish or sell, written for real people with real — and often
unpredictable — schedules.

---

## License

MIT License. Copyright (c) 2026 Asdale Dynamics, LLC. See LICENSE.

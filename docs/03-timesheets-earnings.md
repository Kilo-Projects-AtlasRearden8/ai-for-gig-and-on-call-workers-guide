# 2. Timesheets and earnings tracking

When your schedule changes constantly, paper receipts and memory aren't enough.
You need one place to log every shift: date, start time, end time, breaks, pay
rate, and total earnings. This section shows you how to do that with AI help —
and gives you printable worksheets.

## Step 1: Pick one tracking spot

Choose one place to record shifts and stick with it. Options:

- A printed worksheet (see `worksheets/timesheet-worksheet.html` — print and fill in by hand).
- A simple notes app on your phone.
- A spreadsheet (Google Sheets, Excel, or the free LibreOffice Calc).
- The local `tools/timesheet_tracker.py` script (runs on your computer, nothing
  uploaded).

Pick whichever you'll actually use. A worksheet you forget is worse than a
spreadsheet you don't.

## Step 2: Record every shift the same day

Write down:

1. Date
2. Employer or app (rideshare platform, hospital staffing pool, client name)
3. Start time and end time
4. Break time (unpaid)
5. Total hours worked
6. Pay rate
7. Total earned for the shift
8. Notes (mileage, expenses, tips)

Doing it the same day takes two minutes. Doing it a month later takes an hour
and you'll guess wrong.

## Step 3: Let AI clean up messy notes

If your shift notes are a mess, paste them into a chatbot (without personal
details — use "Client A" instead of real names) and ask:

> "Turn these shift notes into a clean table with date, hours, pay rate, and
> total earned. Leave out names and addresses."

Copy the result into your tracking spot. Always double-check the math yourself —
AI can make arithmetic mistakes.

## Step 4: Review once a week

Pick a low-energy day (Sunday morning with coffee works for many people) and:

- Add up last week's earnings.
- Compare with what the app or employer paid you.
- Note anything missing or wrong while it's still easy to fix.

## Printable worksheets

Open these in your browser and print:

- `static/timesheet.html` — one-page shift log.
- `worksheets/earnings-worksheet.html` — monthly earnings summary.
- `worksheets/shift-swap-worksheet.html` — track who you swapped shifts with.

## Automated option

If you're comfortable with a little setup, `tools/timesheet_tracker.py` lets you
log shifts from your terminal and saves them to a file on your computer. See
`tools/README.md` for instructions.

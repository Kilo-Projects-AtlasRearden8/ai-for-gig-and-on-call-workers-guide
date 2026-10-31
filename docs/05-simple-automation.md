# 4. Simple automation for unpredictable hours

Automation sounds fancy, but it just means "let the computer do the repetitive
part." For irregular schedules, the best automations are small, local, and run
only when you need them.

## Ideas that fit unpredictable hours

- **Shift reminder:** the night before a shift, a script prints tomorrow's
  start time and location to your screen.
- **Earnings summary:** one command adds up this month's earnings from your
  shift log.
- **Message drafts:** AI writes the first version of a client message, a rate
  increase note, or a shift-swap request — you edit and send.
- **Expense tracker:** snap a photo of a receipt, AI extracts the amount and
  category, saves it to your file.

## Start small: one automation

Don't try to automate your whole life. Pick one annoying five-minute task and
automate that. When it works, add another.

## The helper scripts in this project

See `tools/README.md` for the full list and exact commands. Each script:

- Runs on your own computer.
- Saves data only to files on your computer.
- Needs no API keys, no accounts, no internet.
- Comes with tests in `tests/`.

## Step-by-step: weekly earnings summary

If you log shifts in a plain text file or CSV (one line per shift: date, hours,
pay), you can add up a week yourself in three steps:

1. Copy your shifts into a file. Example:

   ```
   2026-10-01, 8, 22.50
   2026-10-03, 6, 22.50
   2026-10-05, 4, 22.50
   ```

2. Run the earnings tracker to see what you've logged:

   ```
   python3 tools/earnings_tracker.py list
   python3 tools/earnings_tracker.py total --month 2026-10
   ```

3. Check the total against your paystub or app earnings before you file
   anything.

You can also paste your shifts into the "weekly earnings summary" on the
Simple automation page of the site — nothing leaves your browser.

Then verify the total yourself. AI drafts, you confirm.

## A note on message drafts

If you want AI to write the first version of a message (a client note, a rate
increase, a shift-swap request), paste the details into a chatbot without real
names or private details, then read and edit the draft yourself before sending.

## Keep it local-first

Because your schedule and earnings are personal, prefer tools that run on your
computer over tools that upload your data. See
[local AI and privacy](./06-local-ai-privacy.md).

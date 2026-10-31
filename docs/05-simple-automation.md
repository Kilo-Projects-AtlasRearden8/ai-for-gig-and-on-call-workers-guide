# 4. Simple automation for unpredictable hours

Automation sounds fancy, but it just means "let the computer do the repetitive
part." For irregular schedules, the best automations are small, local, and run
only when you need them.

## Ideas that fit unpredictable hours

- **Shift reminder:** the night before a shift, a script prints tomorrow's
  schedule to your screen.
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

See `tools/README.md` for the full list. Each script:

- Runs on your own computer.
- Saves data only to files on your computer.
- Needs no API keys, no accounts, no internet.
- Comes with tests in `tests/`.

## A simple example: weekly earnings summary

If you log shifts in a plain text file (one line per shift: date, hours, pay),
you can ask an AI chatbot:

> "Here are my shifts. Add up the total hours and earnings for last week.
> Show the math so I can check it."

Then verify the total yourself. AI drafts, you confirm.

## Keep it local-first

Because your schedule and earnings are personal, prefer tools that run on your
computer over tools that upload your data. See [local AI and privacy](./06-local-ai-privacy.md).

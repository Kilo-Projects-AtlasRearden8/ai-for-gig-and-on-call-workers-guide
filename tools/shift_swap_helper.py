#!/usr/bin/env python3
"""Shift-swap message draft helper.

Prints a short, polite shift-swap message to stdout. Nothing is saved and
nothing is sent. Edit the draft before you send it.
"""

import sys


def draft(name, date, start, end, reason="", offer="", contact=""):
    lines = []
    lines.append("Hi,")
    lines.append(
        f"I'm {name} and I need to swap my shift on {date} "
        f"({fmt_time(start)} - {fmt_time(end)})."
    )
    if reason:
        lines.append(f"Reason: {reason}.")
    if offer:
        lines.append(f"In return: {offer}.")
    if contact:
        lines.append(f"You can reach me at {contact}.")
    lines.append("Please let me know if this works for you.")
    lines.append("Thanks,")
    lines.append(name)
    return "\n".join(lines)


def fmt_time(value):
    if not value:
        return ""
    parts = value.split(":")
    hour = int(parts[0])
    minute = parts[1] if len(parts) > 1 else "00"
    ampm = "pm" if hour >= 12 else "am"
    hour12 = hour % 12 or 12
    return f"{hour12}:{minute} {ampm}"


def main(argv):
    if len(argv) < 5:
        print("Usage: shift_swap_helper.py NAME DATE START END [REASON] [OFFER] [CONTACT]")
        print(
            "Example: shift_swap_helper.py \"Jordan\" 2026-10-04 19:00 07:00 "
            "\"family commitment\" \"I can cover one of your future shifts\""
        )
        return 1
    print(draft(argv[1], argv[2], argv[3], argv[4], argv[5] if len(argv) > 5 else "",
                argv[6] if len(argv) > 6 else "", argv[7] if len(argv) > 7 else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

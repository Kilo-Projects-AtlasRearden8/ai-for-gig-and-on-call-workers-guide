#!/usr/bin/env python3
"""Tests for tools/shift_swap_helper.py"""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))

import shift_swap_helper as ssh


class ShiftSwapHelperTests(unittest.TestCase):
    def test_draft_includes_details(self):
        msg = ssh.draft(
            "Jordan", "2026-10-04", "19:00", "07:00",
            reason="family commitment",
            offer="I can cover one of your future shifts",
            contact="555-0100",
        )
        for part in ["Jordan", "2026-10-04", "7:00 pm", "family commitment",
                     "I can cover one of your future shifts", "555-0100"]:
            self.assertIn(part, msg)

    def test_draft_omits_optional(self):
        msg = ssh.draft("Sam", "2026-10-04", "09:00", "17:00")
        self.assertIn("Sam", msg)
        self.assertNotIn("Reason:", msg)
        self.assertNotIn("In return", msg)

    def test_fmt_time(self):
        self.assertEqual(ssh.fmt_time("19:00"), "7:00 pm")
        self.assertEqual(ssh.fmt_time("07:00"), "7:00 am")
        self.assertEqual(ssh.fmt_time("00:30"), "12:30 am")


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
"""Tests for tools/timesheet_tracker.py"""

import csv
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))

import timesheet_tracker as ttrack


class TimesheetTrackerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
        self.tmp.close()
        ttrack.DATA_FILE = self.tmp.name
        if os.path.exists(self.tmp.name):
            os.remove(self.tmp.name)

    def tearDown(self):
        if os.path.exists(self.tmp.name):
            os.remove(self.tmp.name)

    def test_shift_hours_regular(self):
        self.assertEqual(ttrack.shift_hours("07:00", "15:00"), 8.0)

    def test_shift_hours_overnight(self):
        self.assertEqual(ttrack.shift_hours("19:00", "07:00"), 12.0)

    def test_shift_hours_with_break(self):
        # 8 hours minus 30 min break = 7.5
        hours = round(ttrack.shift_hours("07:00", "15:00") - 30 / 60.0, 2)
        self.assertEqual(hours, 7.5)

    def test_add_and_list(self):
        rc = ttrack.main(["add", "2026-10-01", "07:00", "15:00", "30", "22.50"])
        self.assertEqual(rc, 0)
        shifts = ttrack.load_shifts()
        self.assertEqual(len(shifts), 1)
        self.assertEqual(shifts[0]["date"], "2026-10-01")
        self.assertEqual(float(shifts[0]["hours"]), 7.5)
        self.assertEqual(float(shifts[0]["total"]), 168.75)

    def test_total_all(self):
        ttrack.main(["add", "2026-10-01", "07:00", "15:00", "0", "20.00"])
        ttrack.main(["add", "2026-10-02", "09:00", "17:00", "0", "20.00"])
        rc, _ = self._capture(ttrack.main, ["total"])
        self.assertEqual(rc, 0)

    def test_total_by_month(self):
        ttrack.main(["add", "2026-10-01", "07:00", "15:00", "0", "20.00"])
        ttrack.main(["add", "2026-11-01", "07:00", "15:00", "0", "20.00"])
        shifts = ttrack.load_shifts()
        hours = sum(float(s["hours"]) for s in shifts if s["date"].startswith("2026-10"))
        self.assertEqual(hours, 8.0)

    def test_invalid_date_rejected(self):
        rc = ttrack.main(["add", "not-a-date", "07:00", "15:00", "0", "20.00"])
        self.assertNotEqual(rc, 0)
        self.assertEqual(len(ttrack.load_shifts()), 0)

    def _capture(self, fn, args):
        import io
        old = sys.stdout
        sys.stdout = io.StringIO()
        try:
            rc = fn(args)
        finally:
            sys.stdout = old
        return rc, None


if __name__ == "__main__":
    unittest.main()

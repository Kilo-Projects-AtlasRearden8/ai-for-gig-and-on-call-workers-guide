#!/usr/bin/env python3
"""Tests for tools/earnings_tracker.py"""

import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))

import earnings_tracker as etrack


class EarningsTrackerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
        self.tmp.close()
        etrack.DATA_FILE = self.tmp.name
        if os.path.exists(self.tmp.name):
            os.remove(self.tmp.name)

    def tearDown(self):
        if os.path.exists(self.tmp.name):
            os.remove(self.tmp.name)

    def test_add_and_total(self):
        rc = etrack.main(["add", "2026-10-02", "rideshare app", "180.00"])
        self.assertEqual(rc, 0)
        rows = etrack.load_rows()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["source"], "rideshare app")
        self.assertEqual(float(rows[0]["amount"]), 180.00)

    def test_total_by_month(self):
        etrack.main(["add", "2026-10-02", "app", "100.00"])
        etrack.main(["add", "2026-10-05", "client", "250.00"])
        etrack.main(["add", "2026-11-01", "app", "500.00"])
        rows = [r for r in etrack.load_rows() if r["date"].startswith("2026-10")]
        total = sum(float(r["amount"]) for r in rows)
        self.assertEqual(total, 350.00)

    def test_invalid_amount_rejected(self):
        rc = etrack.main(["add", "2026-10-02", "app", "not-money"])
        self.assertNotEqual(rc, 0)
        self.assertEqual(len(etrack.load_rows()), 0)


if __name__ == "__main__":
    unittest.main()

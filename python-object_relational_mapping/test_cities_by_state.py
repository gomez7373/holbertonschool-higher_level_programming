# Save this as test_cities_by_state.py

import unittest
import subprocess
import os

class TestOutput(unittest.TestCase):
    def setUp(self):
        self.script = "./cities_by_state.py"
        self.db_name = "hbtn_0e_4_usa"
        self.user = "root"
        self.password = "sgc91"
    
    def run_script(self, *args):
        return subprocess.run(
            [self.script, self.user, self.password, self.db_name, *args],
            capture_output=True,
            text=True
        )
    
    def test_output(self):
        expected_output = "(1, 'San Francisco', 'California')\n(2, 'San Jose', 'California')\n(3, 'Los Angeles', 'California')\n(4, 'Fremont', 'California')\n(5, 'Livermore', 'California')\n(6, 'Page', 'Arizona')\n(7, 'Phoenix', 'Arizona')\n(8, 'Dallas', 'Texas')\n(9, 'Houston', 'Texas')\n(10, 'Austin', 'Texas')\n(11, 'New York', 'New York')\n(12, 'Las Vegas', 'Nevada')\n(13, 'Reno', 'Nevada')\n(14, 'Henderson', 'Nevada')\n(15, 'Carson City', 'Nevada')"
        result = self.run_script()
        self.assertEqual(result.stdout.strip(), expected_output.strip(), f"Actual output: {result.stdout.strip()}")

    def test_database_connection_error(self):
        result = subprocess.run(
            [self.script, "wrong_user", "wrong_pass", self.db_name],
            capture_output=True,
            text=True
        )
        self.assertIn("Error connecting to the database", result.stdout, "Database connection error not handled properly!")

    def test_large_number_of_rows(self):
        # This assumes that there are at least 1000 rows in your database.
        # Adjust the number as needed based on your test data.
        result = self.run_script()
        self.assertGreaterEqual(len(result.stdout.splitlines()), 15, "Large number of rows handling issue detected!")

    def test_no_extra_newline(self):
        result = self.run_script()
        output_lines = result.stdout.strip().split("\n")
        self.assertEqual(len(output_lines), 15, "Extra newline detected in output!")

if __name__ == "__main__":
    unittest.main()


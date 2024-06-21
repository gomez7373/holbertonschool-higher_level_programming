"""
Checker script to test the implementation of 4-cities_by_state.py.
This script runs various code quality tools on the student's script,
and then compares the output to the expected output using unittest.
"""

import subprocess
import unittest
from colorama import Fore, Style

def run_command(command):
    """Run a command and return its output and return code."""
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout, result.stderr, result.returncode

def run_pylint(script_name):
    """Run pylint on the specified script and print the output."""
    command = ["pylint", script_name]
    stdout, stderr, returncode = run_command(command)
    print(Fore.BLUE + "Pylint output:\n" + stdout + Style.RESET_ALL)
    if stderr:
        print(Fore.RED + "Pylint errors:\n" + stderr + Style.RESET_ALL)
    return returncode

def run_mypy(script_name):
    """Run mypy on the specified script and print the output."""
    command = ["mypy", script_name]
    stdout, stderr, returncode = run_command(command)
    print(Fore.BLUE + "Mypy output:\n" + stdout + Style.RESET_ALL)
    if stderr:
        print(Fore.RED + "Mypy errors:\n" + stderr + Style.RESET_ALL)
    return returncode

def run_flake8(script_name):
    """Run flake8 on the specified script and print the output."""
    command = ["flake8", script_name]
    stdout, stderr, returncode = run_command(command)
    print(Fore.BLUE + "Flake8 output:\n" + stdout + Style.RESET_ALL)
    if stderr:
        print(Fore.RED + "Flake8 errors:\n" + stderr + Style.RESET_ALL)
    return returncode

def run_black(script_name):
    """Run black on the specified script and print the output."""
    command = ["black", "--check", script_name]
    stdout, stderr, returncode = run_command(command)
    print(Fore.BLUE + "Black output:\n" + stdout + Style.RESET_ALL)
    if stderr:
        print(Fore.RED + "Black errors:\n" + stderr + Style.RESET_ALL)
    return returncode

def run_isort(script_name):
    """Run isort on the specified script and print the output."""
    command = ["isort", "--check-only", script_name]
    stdout, stderr, returncode = run_command(command)
    print(Fore.BLUE + "isort output:\n" + stdout + Style.RESET_ALL)
    if stderr:
        print(Fore.RED + "isort errors:\n" + stderr + Style.RESET_ALL)
    return returncode

def run_pydocstyle(script_name):
    """Run pydocstyle on the specified script and print the output."""
    command = ["pydocstyle", script_name]
    stdout, stderr, returncode = run_command(command)
    print(Fore.BLUE + "Pydocstyle output:\n" + stdout + Style.RESET_ALL)
    if stderr:
        print(Fore.RED + "Pydocstyle errors:\n" + stderr + Style.RESET_ALL)
    return returncode

class TestOutput(unittest.TestCase):
    script_name = "4-cities_by_state.py"
    db_user = "root"
    db_password = "your_password_here"
    db_name = "hbtn_0e_4_usa"
    expected_output = """(1, 'San Francisco', 'California')
(2, 'San Jose', 'California')
(3, 'Los Angeles', 'California')
(4, 'Fremont', 'California')
(5, 'Livermore', 'California')
(6, 'Page', 'Arizona')
(7, 'Phoenix', 'Arizona')
(8, 'Dallas', 'Texas')
(9, 'Houston', 'Texas')
(10, 'Austin', 'Texas')
(11, 'New York', 'New York')
(12, 'Las Vegas', 'Nevada')
(13, 'Reno', 'Nevada')
(14, 'Henderson', 'Nevada')
(15, 'Carson City', 'Nevada')"""

    def test_output(self):
        """Run the student's script and compare the output to the expected output."""
        command = [f"./{self.script_name}", self.db_user, self.db_password, self.db_name]
        result = subprocess.run(command, capture_output=True, text=True)
        if result.stdout.strip() == self.expected_output.strip():
            print(Fore.GREEN + "Output test: Passed" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Output test: Failed" + Style.RESET_ALL)
            print(Fore.RED + f"Expected: {self.expected_output.strip()}" + Style.RESET_ALL)
            print(Fore.RED + f"Actual: {result.stdout.strip()}" + Style.RESET_ALL)
        self.assertEqual(result.stdout.strip(), self.expected_output.strip(), f"Actual output: {result.stdout.strip()}")

    def test_sql_injection(self):
        """Test to ensure the script is not vulnerable to SQL injection."""
        command = [f"./{self.script_name}", self.db_user, self.db_password, self.db_name, "'; DROP TABLE states; --"]
        result = subprocess.run(command, capture_output=True, text=True)
        if "'; DROP TABLE states; --" not in result.stdout:
            print(Fore.GREEN + "SQL injection protection test: Passed" + Style.RESET_ALL)
        else:
            print(Fore.RED + "SQL injection protection test: Failed" + Style.RESET_ALL)
        self.assertNotIn("'; DROP TABLE states; --", result.stdout, "SQL injection vulnerability detected!")

    def test_no_extra_newline(self):
        """Ensure no extra newline is printed in the output."""
        command = [f"./{self.script_name}", self.db_user, self.db_password, self.db_name]
        result = subprocess.run(command, capture_output=True, text=True)
        output_lines = result.stdout.splitlines()
        if len(output_lines) == 15:
            print(Fore.GREEN + "No extra newline test: Passed" + Style.RESET_ALL)
        else:
            print(Fore.RED + "No extra newline test: Failed" + Style.RESET_ALL)
        self.assertEqual(len(output_lines), 15, "Extra newline detected in output!")

    def test_database_connection_error(self):
        """Test handling of database connection errors."""
        command = [f"./{self.script_name}", "wrong_user", "wrong_password", self.db_name]
        result = subprocess.run(command, capture_output=True, text=True)
        if "Error connecting to the database" in result.stderr:
            print(Fore.GREEN + "Database connection error handling test: Passed" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Database connection error handling test: Failed" + Style.RESET_ALL)
        self.assertIn("Error connecting to the database", result.stderr, "Database connection error not handled properly!")

    def test_empty_table(self):
        """Test handling of an empty table."""
        command = [f"./{self.script_name}", self.db_user, self.db_password, "hbtn_0e_4_empty"]
        result = subprocess.run(command, capture_output=True, text=True)
        if result.stdout.strip() == "":
            print(Fore.GREEN + "Empty table handling test: Passed" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Empty table handling test: Failed" + Style.RESET_ALL)
        self.assertEqual(result.stdout.strip(), "", "The script should handle empty tables correctly.")

    def test_special_characters(self):
        """Test handling of special characters in the table."""
        command = [f"./{self.script_name}", self.db_user, self.db_password, "hbtn_0e_4_special"]
        result = subprocess.run(command, capture_output=True, text=True)
        if "\n\n" not in result.stdout:
            print(Fore.GREEN + "Special characters handling test: Passed" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Special characters handling test: Failed" + Style.RESET_ALL)
        self.assertNotIn("\n\n", result.stdout, "Special characters handling issue detected!")

    def test_large_number_of_rows(self):
        """Test handling of a large number of rows in the table."""
        command = [f"./{self.script_name}", self.db_user, self.db_password, "hbtn_0e_4_large"]
        result = subprocess.run(command, capture_output=True, text=True)
        if len(result.stdout.splitlines()) >= 1000:
            print(Fore.GREEN + "Large number of rows handling test: Passed" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Large number of rows handling test: Failed" + Style.RESET_ALL)
        self.assertGreaterEqual(len(result.stdout.splitlines()), 1000, "Large number of rows handling issue detected!")

if __name__ == "__main__":
    script_name = "4-cities_by_state.py"
    
    print(Fore.YELLOW + "Running Pylint..." + Style.RESET_ALL)
    pylint_returncode = run_pylint(script_name)
    if pylint_returncode == 0 or pylint_returncode == 2:  # Allow filename warning
        print(Fore.GREEN + "Pylint check: Passed (ignoring filename warning)" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"Pylint check: Failed. Run: $ pylint {script_name}" + Style.RESET_ALL)

    print(Fore.YELLOW + "Running Mypy..." + Style.RESET_ALL)
    mypy_returncode = run_mypy(script_name)
    if mypy_returncode == 0:
        print(Fore.GREEN + "Mypy check: Passed" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"Mypy check: Failed. Run: $ mypy {script_name}" + Style.RESET_ALL)

    print(Fore.YELLOW + "Running Flake8..." + Style.RESET_ALL)
    flake8_returncode = run_flake8(script_name)
    if flake8_returncode == 0:
        print(Fore.GREEN + "Flake8 check: Passed" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"Flake8 check: Failed. Run: $ flake8 --config=.flake8 {script_name}" + Style.RESET_ALL)

    print(Fore.YELLOW + "Running Black..." + Style.RESET_ALL)
    black_returncode = run_black(script_name)
    if black_returncode == 0:
        print(Fore.GREEN + "Black check: Passed" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"Black check: Failed. Run: $ black {script_name}" + Style.RESET_ALL)

    print(Fore.YELLOW + "Running Isort..." + Style.RESET_ALL)
    isort_returncode = run_isort(script_name)
    if isort_returncode == 0:
        print(Fore.GREEN + "isort check: Passed" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"isort check: Failed. Run: $ isort {script_name}" + Style.RESET_ALL)

    print(Fore.YELLOW + "Running Pydocstyle..." + Style.RESET_ALL)
    pydocstyle_returncode = run_pydocstyle(script_name)
    if pydocstyle_returncode == 0:
        print(Fore.GREEN + "Pydocstyle check: Passed" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"Pydocstyle check: Failed. Run: $ pydocstyle {script_name}" + Style.RESET_ALL)

    print(Fore.YELLOW + "Running Unit Tests..." + Style.RESET_ALL)
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


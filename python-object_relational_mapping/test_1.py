"""
Checker script to test the implementation of 1-filter_states.py.
This script runs pylint, mypy, flake8, black, and isort on the student's script,
and then compares the output to the expected output using unittest.
"""

import subprocess
import unittest

def run_command(command):
    """Run a command and return its output and return code."""
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout, result.stderr, result.returncode

def run_pylint():
    """Run pylint on the 1-filter_states.py file and print the output."""
    command = ["pylint", "1-filter_states.py"]
    stdout, stderr, returncode = run_command(command)
    print("Pylint output:\n", stdout)
    if stderr:
        print("Pylint errors:\n", stderr)
    return returncode

def run_mypy():
    """Run mypy on the 1-filter_states.py file and print the output."""
    command = ["mypy", "1-filter_states.py"]
    stdout, stderr, returncode = run_command(command)
    print("Mypy output:\n", stdout)
    if stderr:
        print("Mypy errors:\n", stderr)
    return returncode

def run_flake8():
    """Run flake8 on the 1-filter_states.py file and print the output."""
    command = ["flake8", "1-filter_states.py"]
    stdout, stderr, returncode = run_command(command)
    print("Flake8 output:\n", stdout)
    if stderr:
        print("Flake8 errors:\n", stderr)
    return returncode

def run_black():
    """Run black on the 1-filter_states.py file and print the output."""
    command = ["black", "--check", "1-filter_states.py"]
    stdout, stderr, returncode = run_command(command)
    print("Black output:\n", stdout)
    if stderr:
        print("Black errors:\n", stderr)
    return returncode

def run_isort():
    """Run isort on the 1-filter_states.py file and print the output."""
    command = ["isort", "--check-only", "1-filter_states.py"]
    stdout, stderr, returncode = run_command(command)
    print("isort output:\n", stdout)
    if stderr:
        print("isort errors:\n", stderr)
    return returncode

class TestOutput(unittest.TestCase):
    def test_output(self):
        """Run the student's script and compare the output to the expected output."""
        # Define the command and arguments to run the student's script
        command = ["./1-filter_states.py", "root", "sgc91", "hbtn_0e_0_usa"]

        # Run the student's script and capture the output
        result = subprocess.run(command, capture_output=True, text=True)

        # Expected output based on the initial data in the database
        expected_output = """(4, 'New York')
(5, 'Nevada')
"""

        # Compare the actual output to the expected output
        self.assertEqual(result.stdout.strip(), expected_output.strip(), f"Actual output: {result.stdout.strip()}")

if __name__ == "__main__":
    pylint_returncode = run_pylint()
    if pylint_returncode == 0 or pylint_returncode == 2:  # Allow filename warning
        print("Pylint check: Passed (ignoring filename warning)")
    else:
        print("Pylint check: Failed. Run: $ pylint 1-filter_states.py")

    mypy_returncode = run_mypy()
    if mypy_returncode == 0:
        print("Mypy check: Passed")
    else:
        print("Mypy check: Failed. Run: $ mypy 1-filter_states.py")

    flake8_returncode = run_flake8()
    if flake8_returncode == 0:
        print("Flake8 check: Passed")
    else:
        print("Flake8 check: Failed. Run: $ flake8 1-filter_states.py")

    black_returncode = run_black()
    if black_returncode == 0:
        print("Black check: Passed")
    else:
        print("Black check: Failed. Run: $ black 1-filter_states.py")

    isort_returncode = run_isort()
    if isort_returncode == 0:
        print("isort check: Passed")
    else:
        print("isort check: Failed. Run: $ isort 1-filter_states.py")

    if (pylint_returncode in [0, 2] and mypy_returncode == 0 and flake8_returncode == 0 and
        black_returncode == 0 and isort_returncode == 0):
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
    else:
        print("Fix style and type check issues before running the checker.")

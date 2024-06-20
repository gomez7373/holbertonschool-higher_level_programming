"""
Checker script to test the implementation of 4-cities_by_state.py.
This script runs pylint, mypy, flake8, black, and isort on the student's script,
and then compares the output to the expected output using unittest.
"""

import subprocess
import unittest
from colorama import Fore, Style

def run_command(command):
    """Run a command and return its output and return code."""
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout, result.stderr, result.returncode

def run_pylint():
    """Run pylint on the 4-cities_by_state.py file and print the output."""
    command = ["pylint", "4-cities_by_state.py"]
    stdout, stderr, returncode = run_command(command)
    print(Fore.BLUE + "Pylint output:\n" + stdout + Style.RESET_ALL)
    if stderr:
        print(Fore.RED + "Pylint errors:\n" + stderr + Style.RESET_ALL)
    return returncode

def run_mypy():
    """Run mypy on the 4-cities_by_state.py file and print the output."""
    command = ["mypy", "4-cities_by_state.py"]
    stdout, stderr, returncode = run_command(command)
    print(Fore.BLUE + "Mypy output:\n" + stdout + Style.RESET_ALL)
    if stderr:
        print(Fore.RED + "Mypy errors:\n" + stderr + Style.RESET_ALL)
    return returncode

def run_flake8():
    """Run flake8 on the 4-cities_by_state.py file and print the output."""
    command = ["flake8", "4-cities_by_state.py"]
    stdout, stderr, returncode = run_command(command)
    print(Fore.BLUE + "Flake8 output:\n" + stdout + Style.RESET_ALL)
    if stderr:
        print(Fore.RED + "Flake8 errors:\n" + stderr + Style.RESET_ALL)
    return returncode

def run_black():
    """Run black on the 4-cities_by_state.py file and print the output."""
    command = ["black", "--check", "4-cities_by_state.py"]
    stdout, stderr, returncode = run_command(command)
    print(Fore.BLUE + "Black output:\n" + stdout + Style.RESET_ALL)
    if stderr:
        print(Fore.RED + "Black errors:\n" + stderr + Style.RESET_ALL)
    return returncode

def run_isort():
    """Run isort on the 4-cities_by_state.py file and print the output."""
    command = ["isort", "--check-only", "4-cities_by_state.py"]
    stdout, stderr, returncode = run_command(command)
    print(Fore.BLUE + "isort output:\n" + stdout + Style.RESET_ALL)
    if stderr:
        print(Fore.RED + "isort errors:\n" + stderr + Style.RESET_ALL)
    return returncode

class TestOutput(unittest.TestCase):
    def test_output(self):
        """Run the student's script and compare the output to the expected output."""
        # Define the command and arguments to run the student's script
        command = ["./4-cities_by_state.py", "root", "your_password_here", "hbtn_0e_4_usa"]

        # Run the student's script and capture the output
        result = subprocess.run(command, capture_output=True, text=True)

        # Expected output based on the initial data in the database
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
(15, 'Carson City', 'Nevada')
"""

        # Compare the actual output to the expected output
        self.assertEqual(result.stdout.strip(), expected_output.strip(), f"Actual output: {result.stdout.strip()}")

if __name__ == "__main__":
    pylint_returncode = run_pylint()
    if pylint_returncode == 0 or pylint_returncode == 2:  # Allow filename warning
        print(Fore.GREEN + "Pylint check: Passed (ignoring filename warning)" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Pylint check: Failed. Run: $ pylint 4-cities_by_state.py" + Style.RESET_ALL)

    mypy_returncode = run_mypy()
    if mypy_returncode == 0:
        print(Fore.GREEN + "Mypy check: Passed" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Mypy check: Failed. Run: $ mypy 4-cities_by_state.py" + Style.RESET_ALL)

    flake8_returncode = run_flake8()
    if flake8_returncode == 0:
        print(Fore.GREEN + "Flake8 check: Passed" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Flake8 check: Failed. Run: $ flake8 --config=.flake8 4-cities_by_state.py" + Style.RESET_ALL)

    black_returncode = run_black()
    if black_returncode == 0:
        print(Fore.GREEN + "Black check: Passed" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Black check: Failed. Run: $ black 4-cities_by_state.py" + Style.RESET_ALL)

    isort_returncode = run_isort()
    if isort_returncode == 0:
        print(Fore.GREEN + "isort check: Passed" + Style.RESET_ALL)
    else:
        print(Fore.RED + "isort check: Failed. Run: $ isort 4-cities_by_state.py" + Style.RESET_ALL)

    if (pylint_returncode in [0, 2] and mypy_returncode == 0 and flake8_returncode == 0 and
        black_returncode == 0 and isort_returncode == 0):
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
    else:
        print(Fore.RED + "Fix style and type check issues before running the checker." + Style.RESET_ALL)


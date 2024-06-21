"""
Checker script to test the implementation of 3-my_safe_filter_states.py.
This script runs pylint, mypy, flake8, black, and isort on the student's script,
and then compares the output to the expected output using unittest.
"""

import subprocess
import unittest
from colorama import init, Fore, Style

# Initialize colorama
init()

def run_command(command):
    """Run a command and return its output and return code."""
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout, result.stderr, result.returncode

def run_pylint():
    """Run pylint on the 3-my_safe_filter_states.py file and print the output."""
    command = ["pylint", "3-my_safe_filter_states.py"]
    stdout, stderr, returncode = run_command(command)
    print(Fore.BLUE + "Pylint output:\n" + Style.RESET_ALL + stdout)
    if stderr:
        print(Fore.RED + "Pylint errors:\n" + Style.RESET_ALL + stderr)
    return returncode

def run_mypy():
    """Run mypy on the 3-my_safe_filter_states.py file and print the output."""
    command = ["mypy", "3-my_safe_filter_states.py"]
    stdout, stderr, returncode = run_command(command)
    print(Fore.BLUE + "Mypy output:\n" + Style.RESET_ALL + stdout)
    if stderr:
        print(Fore.RED + "Mypy errors:\n" + Style.RESET_ALL + stderr)
    return returncode

def run_flake8():
    """Run flake8 on the 3-my_safe_filter_states.py file and print the output."""
    command = ["flake8", "--config=.flake8", "3-my_safe_filter_states.py"]
    stdout, stderr, returncode = run_command(command)
    print(Fore.BLUE + "Flake8 output:\n" + Style.RESET_ALL + stdout)
    if stderr:
        print(Fore.RED + "Flake8 errors:\n" + Style.RESET_ALL + stderr)
    return returncode

def run_black():
    """Run black on the 3-my_safe_filter_states.py file and print the output."""
    command = ["black", "--check", "3-my_safe_filter_states.py"]
    stdout, stderr, returncode = run_command(command)
    print(Fore.BLUE + "Black output:\n" + Style.RESET_ALL + stdout)
    if stderr:
        print(Fore.RED + "Black errors:\n" + Style.RESET_ALL + stderr)
    return returncode

def run_isort():
    """Run isort on the 3-my_safe_filter_states.py file and print the output."""
    command = ["isort", "--check-only", "3-my_safe_filter_states.py"]
    stdout, stderr, returncode = run_command(command)
    print(Fore.BLUE + "isort output:\n" + Style.RESET_ALL + stdout)
    if stderr:
        print(Fore.RED + "isort errors:\n" + Style.RESET_ALL + stderr)
    return returncode

class TestOutput(unittest.TestCase):
    def test_output(self):
        """Run the student's script and compare the output to the expected output."""
        # Define the command and arguments to run the student's script
        command = ["./3-my_safe_filter_states.py", "root", "sgc91", "hbtn_0e_0_usa", "Arizona"]

        # Run the student's script and capture the output
        result = subprocess.run(command, capture_output=True, text=True)

        # Expected output based on the initial data in the database
        expected_output = """(2, 'Arizona')
"""

        # Compare the actual output to the expected output
        self.assertEqual(result.stdout.strip(), expected_output.strip(), f"Actual output: {result.stdout.strip()}")

if __name__ == "__main__":
    pylint_returncode = run_pylint()
    if pylint_returncode == 0 or pylint_returncode == 2:  # Allow filename warning
        print(Fore.GREEN + "Pylint check: Passed (ignoring filename warning)" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Pylint check: Failed. Run: $ pylint 3-my_safe_filter_states.py" + Style.RESET_ALL)

    mypy_returncode = run_mypy()
    if mypy_returncode == 0:
        print(Fore.GREEN + "Mypy check: Passed" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Mypy check: Failed. Run: $ mypy 3-my_safe_filter_states.py" + Style.RESET_ALL)

    flake8_returncode = run_flake8()
    if flake8_returncode == 0:
        print(Fore.GREEN + "Flake8 check: Passed" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Flake8 check: Failed. Run: $ flake8 --config=.flake8 3-my_safe_filter_states.py" + Style.RESET_ALL)

    black_returncode = run_black()
    if black_returncode == 0:
        print(Fore.GREEN + "Black check: Passed" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Black check: Failed. Run: $ black 3-my_safe_filter_states.py" + Style.RESET_ALL)

    isort_returncode = run_isort()
    if isort_returncode == 0:
        print(Fore.GREEN + "isort check: Passed" + Style.RESET_ALL)
    else:
        print(Fore.RED + "isort check: Failed. Run: $ isort 3-my_safe_filter_states.py" + Style.RESET_ALL)

    if (pylint_returncode in [0, 2] and mypy_returncode == 0 and flake8_returncode == 0 and
        black_returncode == 0 and isort_returncode == 0):
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
    else:
        print(Fore.RED + "Fix style and type check issues before running the checker." + Style.RESET_ALL)
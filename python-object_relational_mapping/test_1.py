"""
Checker script to test the implementation of 1-filter_states.py.
This script runs pylint on the student's script and then compares the output to the expected output.
"""

import subprocess

def run_pylint():
    """Run pylint on the 1-filter_states.py file and print the output."""
    command = ["pylint", "1-filter_states.py"]
    result = subprocess.run(command, capture_output=True, text=True)
    print("Pylint output:\n", result.stdout)
    return result.returncode

def run_checker():
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
    if result.stdout.strip() == expected_output.strip():
        print("Test passed!")
    else:
        print("Test failed!")
        print("Expected output:")
        print(expected_output)
        print("Actual output:")
        print(result.stdout.strip())

if __name__ == "__main__":
    pylint_returncode = run_pylint()
    if pylint_returncode == 0:
        run_checker()
    else:
        print("Fix pylint issues before running the checker.")


"""
Checker script to test the implementation of 0-select_states.py.
This script runs the student's script and compares the output to the expected output.
"""

import subprocess

def run_checker():
    # Define the command and arguments to run the student's script
    command = ["./0-select_states.py", "root", "root", "hbtn_0e_0_usa"]

    # Run the student's script and capture the output
    result = subprocess.run(command, capture_output=True, text=True)

    # Expected output based on the initial data in the database
    expected_output = """(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
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
        print(result.stdout)

if __name__ == "__main__":
    run_checker()

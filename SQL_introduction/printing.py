import os

def print_sql_file_content(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"Content of {file_name}:\n{content}\n")
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def print_all_sql_files_in_current_directory():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    try:
        for file_name in os.listdir(current_directory):
            if file_name.endswith('.sql'):
                print_sql_file_content(file_name)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print_all_sql_files_in_current_directory()

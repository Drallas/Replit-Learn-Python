# Make for each file in files an import statement like below.

from files.programming_languages import display_language
from files.read_csv import read_csv
from files.write_json import data, test_json_write

# Ask what python file to run
print("What python file do you want to run?")
print("Options: write_json, programming_languages, read_csv")
file_to_run = input()

# Dictionary for actions
actions = {
    "write_json":
    lambda: [test_json_write(data),
             print("Creating json file...!")],
    "programming_languages":
    lambda: print(f"Hello {display_language()} coder!"),
    "read_csv": lambda: print(read_csv())
}

# Run the selected action
if file_to_run in actions:
    actions[file_to_run]()
else:
    print("Invalid file name.")  # Ask what python file to run

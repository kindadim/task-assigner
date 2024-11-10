import os
import sys

# Add the subdirectory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'shuffler'))

# Now we can import from shuffler.py
import shuffler

def main(title_file, task_file):
    print("Executing from main.py")
    # Call function from shuffler.py
    shuffler.assign(title_file, task_file)

if __name__ == "__main__":
    main(
    'shuffler/config/titles.txt',
    # File containing name and assignment weight
    'shuffler/config/tasks.txt')
    # File containing list of tasks
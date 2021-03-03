import os

os.chdir('pylearning')

current_directory = os.getcwd()
filepath = os.path.join(current_directory, 'displaydatedirs.py')
exception_stats = os.stat(filepath)

print(current_directory)
print(filepath)
print(exception_stats)
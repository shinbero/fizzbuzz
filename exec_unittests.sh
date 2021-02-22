# Find all test scripts and execute them.
find tests -name 'test*.py' | xargs python -m unittest

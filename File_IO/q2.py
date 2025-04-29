#Check File Exists
# Write a program that checks if a file named myfile.txt exists, and prints a message accordingly.

import os

filename = "myfile.txt"

if os.path.exists(filename):
    print(f"{filename} exists.")
else:
    print(f"{filename} does not exist.")



#Better approach
from pathlib import Path

file = Path("myfile.txt")

if file.exists():
    print(f"{file} exists.")
else:
    print(f"{file} does not exist.")



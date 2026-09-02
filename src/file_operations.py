import os
from ui.colors import color_text

def check_file_directory():

    file_results = []

    for item in os.listdir('.'):

        if item == '.git':
            continue

        file_results.append(item)

    if file_results:
        print("\nDirectory Contents:")

        for item in file_results:
            print(item)

        return True

    else:
        color_text("\nWarning: This repository contains no project files.", "red")
        color_text("Please add at least one file before attempting to stage, commit, or push.", "yellow")

        return False

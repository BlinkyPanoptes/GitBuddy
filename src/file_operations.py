import os
from ui.colors import color_text

def check_file_directory():

    file_results = [item for item in os.listdir('.') if item != '.git']

    if file_results:
        return True

    color_text("\nWarning: This repository contains no project files.", "red")
    color_text("Please add at least one file before attempting to stage, commit, or push.", "yellow")

    return False

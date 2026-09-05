import subprocess
from git_operations import get_repository_status, collect_staged_files
from ui.tables import print_staging_table, print_confirm_stage_table
from ui.colors import color_text, console

# Stages every change in the working directory (git add .)
def git_add_stages():
    stage_results = subprocess.run(['git', 'add', '.'], capture_output = True, text = True)

    if stage_results.returncode == 0:
        return collect_staged_files()
    else:
        return None

# Stages only the given filenames (git add <file1> <file2> ...)
def git_add_specific(files):
    add_results = subprocess.run(['git', 'add'] + files, capture_output = True, text = True)

    if add_results.returncode == 0:
        return collect_staged_files()
    else:
        return None

# Interactive staging menu, called from main.py option "2".
# Lets the user choose between staging everything or specific files.
def stage_changes():
    status = get_repository_status()

    if status is None:
        color_text("\nFailed to retrieve repository status.", "red")
        return

    if not status:
        color_text("\nThere are no changes to stage.", "yellow")
        color_text("Please add a file or make a change before staging", "yellow")
        return

    print_staging_table()
    user_choice = console.input("\n[bold cyan]Select an option > [/bold cyan]")

    if user_choice == "1":
        staged_status = git_add_stages()

    elif user_choice == "2":
        files_input = console.input("\n[bold cyan]Type the file(s) to stage, separated by spaces > [/bold cyan]")
        files = files_input.split()

        if not files:
            color_text("\nNo files entered.", "yellow")
            return

        color_text("\nAttention: You are about to stage the following files:", "yellow")
        status_lookup = {item['file']: item for item in status}

        files_with_status = []

        for file in files:
            entry = status_lookup.get(file, {'status': 'unknown', 'color': 'white'})

            files_with_status.append({
                'file': file,
                'status': entry['status'],
                'color': entry['color']
            })

        print_confirm_stage_table(files_with_status, "\nFiles to be staged")
        confirm = console.input("\n[bold cyan]Are you sure you want to continue? (y/n) > [/bold cyan]")

        if confirm.lower() != 'y':
            color_text("\nStaging canceled.", "yellow")
            return

        staged_status = git_add_specific(files)

    else:
        color_text("\nInvalid option.", "red")
        return

    if staged_status is not None:
        print_confirm_stage_table(staged_status, "\nSuccessfully staged files:")

    else:
        color_text("\nFailed to stage changes.", "red")

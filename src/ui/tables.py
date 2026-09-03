from rich.table import Table
from ui.colors import console

# Build Menu of Main
def build_menu_table():
    table = Table(title="\nWelcome to GitPal")

    table.add_column("Option", justify="center", style="bold yellow")
    table.add_column("Action", style="white")

    table.add_row("1", "Repository Status")
    table.add_row("2", "Stage Changes")
    table.add_row("3", "Commit Changes")
    table.add_row("4", "Push Changes")
    table.add_row("5", "Remote Repository")
    table.add_row("6", "Exit")

    return table


def print_menu_table():
    console.print(build_menu_table())

# Build Menu of Staging
def build_staging_table():

    table = Table(title="\nStage Changes")

    table.add_column("Option", justify="center", style="bold yellow")
    table.add_column("Action", style="white")

    table.add_row("1", "Stage All Changes")
    table.add_row("2", "Stage Specific Changes")

    return table

def print_staging_table():
    console.print(build_staging_table())

# Build confirmation table listing files about to be staged or committed, given a title
def build_confirm_stage_table(files_with_status, title):
    table = Table(title=title)

    table.add_column("#", justify="center", style="bold yellow")
    table.add_column("File", style="white")
    table.add_column("Status", style="white")

    for index, item in enumerate(files_with_status, start=1):
        status_text = f"[{item['color']}]{item['status']}[/{item['color']}]"
        table.add_row(str(index), item['file'], status_text)

    return table

def print_confirm_stage_table(files_with_status, title):
    console.print(build_confirm_stage_table(files_with_status, title))

def print_confirm_commit_table(files_with_status):
    console.print(build_confirm_stage_table(files_with_status, "\nFiles to be committed"))

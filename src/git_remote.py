import subprocess
from ui.loading import loading_screen
from ui.colors import color_text, console
from ui.tables import print_remote_table
import time

def has_git_remote():
    # Check if the Git repository has a remote
    check_git_remote = subprocess.run(['git', 'remote'], capture_output=True, text=True)

    if check_git_remote.stdout.strip():
        return True
    else:
        return False

def git_remote_origin(remote_url):
    # Command to add Git repository origin
    add_remote = subprocess.run(['git', 'remote', 'add', 'origin', remote_url], capture_output=True, text=True)

    if add_remote.returncode == 0:
        return True
    else:
        return False

def verify_git_remote(remote_url):
    # This is the function to check if the repository exists and is accessible

    check_repository = subprocess.run(['gh', 'repo', 'view', remote_url], capture_output = True, text = True)

    if check_repository.returncode == 0:
        return True
    else:
        return False

def change_git_remote(remote_url):
    change_remote = subprocess.run(['git', 'remote', 'set-url', 'origin', remote_url], capture_output = True, text = True)

    if change_remote.returncode == 0:
        return True
    else:
        return False

# This is the function where you can view, change or remove the origin of the remote
def remote_repository():
    while True:

        current_remote = subprocess.run(['git', 'remote', '-v'], capture_output = True, text = True)

        console.print(f"\n[bold cyan]Current Remote:[/bold cyan]\n{current_remote.stdout.strip()}")
        print_remote_table()

        user_input = console.input("\n[bold cyan]Select an option > [/bold cyan]")

        if user_input == "1":
            # Change remote
            user_input = console.input("\n[bold cyan]Are you sure you would like to change remote origin? (y/n) > [/bold cyan]")

            if user_input.lower() == "y":

                new_remote_origin = console.input("\n[bold cyan]Please paste your new remote link here > [/bold cyan]")

                print()
                loading_screen("Verifying the new remote repository: ")

                if verify_git_remote(new_remote_origin):

                    loading_screen("Changing the remote repository: ")

                    if change_git_remote(new_remote_origin):
                        color_text("Successfully changed the remote repository.", "green")
                    else:
                        color_text("Failed to connect to the new remote repository.", "red")

                    time.sleep(2)

                else:
                    color_text("The GitHub repository could not be found or accessed.", "yellow")
                    color_text("Please check the repository URL and your GitHub permissions.", "yellow")

                    time.sleep(2)

        elif user_input == "2":
            # Back to main menu
            break

        else:
            print("\nInvalid option. Please try again.")
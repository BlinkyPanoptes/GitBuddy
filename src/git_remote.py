import subprocess
from ui.loading import loading_screen
from ui.colors import color_text
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

        print("\n================================")
        print("       Remote Repository")
        print("================================")

        if current_remote.returncode == 0:
            print("\nCurrent Remote:")
            print(current_remote.stdout.strip())
        else:
            color_text("\nNo remote repository is configured.", "yellow")

        print("\n================================")
        print("[1] Change Remote")
        print("[2] Back")
        print("================================")

        user_input = input("Select an option: ")

        if user_input == "1":
            # Change remote
            user_input = input("\nAre you sure you would like to change remote origin? [y/n]: ")

            if user_input.lower() == "y":

                new_remote_origin = input("\nPlease paste your new remote link here: ")

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
import subprocess
from ui.loading import loading_screen
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

        loading_screen("Checking current remote repository")

        current_remote = subprocess.run(['git', 'remote', '-v'], capture_output = True, text = True)

        print("\n================================")
        print("       Remote Repository")
        print("================================")

        if current_remote.returncode == 0:
            print("\nCurrent Remote:")
            print(current_remote.stdout.strip())
        else:
            print("\nNo remote repository is configured.")

        print("\n================================")
        print("[1] Change Remote")
        print("[2] Back")
        print("================================\n")

        user_input = input("Select an option: ")

        if user_input == "1":
            # Change remote
            user_input = input("Would you like to change remote origin? [y/n]: ")

            if user_input.lower() == "y":

                new_remote_origin = input("Please paste your new remote link here: ")

                loading_screen("Verifying the new remote repository")

                if verify_git_remote(new_remote_origin):

                    loading_screen("Changing the remote repository")

                    if change_git_remote(new_remote_origin):
                        print("Successfully changed the remote repository.")
                    else:
                        print("Failed to connect to the new remote repository.")

                    time.sleep(2)

                else:
                    print("\nThe GitHub repository could not be found or accessed.")
                    print("Please check the repository URL and your GitHub permissions.")

                    time.sleep(2)

        elif user_input == "2":
            # Back to main menu
            break

        else:
            print("Invalid option. Please try again.")
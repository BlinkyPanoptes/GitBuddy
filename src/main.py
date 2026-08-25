import subprocess
from git_auth import is_github_authenticated, authenticate_github
from git_remote import has_git_remote, git_remote_origin
from git_operations import get_repository_status
import sys

def is_git_repository():
    # Run the git command 'git rev-parse --is-inside-work-tree'
    check_git_repo = subprocess.run(
        ['git', 'rev-parse', '--is-inside-work-tree'],
        capture_output=True,
        text=True
    )

    # Condition to check if the command worked (return code 0)
    if check_git_repo.returncode == 0:
        return True
    else:
        return False

# Main Menu
def main_menu():
    while True:
        print("\n================================")
        print("           GitBuddy")
        print("================================")
        print("1. Repository Status")
        print("2. Exit")
        print("================================")

        user_choice = input("Select an option: ")

        if user_choice == "1":

            status = get_repository_status()

            if status is None:
                print("Failed to retrieve repository status.")

            elif not status:
                print("Working tree is clean.")

            else:
                print("\nRepository Changes:")

                for item in status:
                    print(f"{item['status']}: {item['file']}")

                    user_input = input("Back to Main Menu?(y/n): ")

                    if user_input.lower() == 'y':
                        main_menu()
                    else:
                        print("Exiting GitBuddy.")
                        sys.exit()

        elif user_choice == "2":
            print("Exiting GitBuddy.")
            sys.exit()

        else:
            print("Invalid option. Please try again.")


# Main program execution
if __name__ == "__main__":

    # ==========================================
    # 1. CHECK GITHUB AUTHENTICATION
    # ==========================================

    if is_github_authenticated():
        print("GitHub account is already authenticated.")

    else:
        print("GitHub is not yet authenticated.")

        user_auth_answer = input(
            "Do you want to authenticate with GitHub? (y/n): "
        )

        if user_auth_answer.lower() == 'y':

            if authenticate_github():
                print("Successfully authenticated with GitHub.")

            else:
                print("GitHub authentication failed.")
                sys.exit()

        else:
            print("GitHub authentication canceled.")
            sys.exit()


    # ==========================================
    # 2. CHECK LOCAL GIT REPOSITORY
    # ==========================================

    if is_git_repository():
        print("This is a Git repository.")

    else:
        print("This is not a Git repository.")

        user_answer = input(
            "Do you want to initialize a new Git repository here? (y/n): "
        )

        if user_answer.lower() == 'y':

            # Run the git command 'git init'
            init_git_repo = subprocess.run(
                ['git', 'init'],
                capture_output=True,
                text=True
            )

            if init_git_repo.returncode == 0:
                print("Successfully initialized a new Git repository.")

                # Check if the repository is now initialized
                if is_git_repository():
                    print("This is now a Git repository.")
                else:
                    print("Failed to verify the Git repository initialization.")

            else:
                print(
                    "Failed to initialize a Git repository. "
                    "Error:",
                    init_git_repo.stderr
                )

        else:
            print("Git repository initialization canceled.")
            sys.exit()

    # ==========================================
    # 3. CHECK GIT REMOTE
    # ==========================================

    if has_git_remote():
        print("This Git repository is connected to a remote repository.")
    else:
        print("This Git repository is not connected to any remote repository.")

        user_input = input("Do you want to connect this into an existing remote repository?(y/n): ")

        if user_input.lower() == 'y':
            remote_origin_input = input("Paste your remote origin repository link here: ")

            if git_remote_origin(remote_origin_input):
                print("Successfully connected to the remote repository.")

            else:
                print("Failed to connect to the remote repository")

        else:
            print("Remote repository connection canceled.")

    # ==========================================
    # 4. MAIN MENU
    # ==========================================

    main_menu()
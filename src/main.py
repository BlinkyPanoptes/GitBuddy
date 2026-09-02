import subprocess
from git_auth import is_github_authenticated, authenticate_github
from git_remote import has_git_remote, git_remote_origin, remote_repository, verify_git_remote
from git_operations import get_repository_status, git_add_stages, stages_changes, git_push_changes, has_staged_changes, is_git_repository
from file_operations import check_file_directory
from ui.loading import loading_screen
from ui.colors import color_text
import time
import sys

# Back to Main Menu
def return_to_menu():
    user_input = input("\nBack to Main Menu? [y/n]: ")

    if user_input.lower() != 'y':
        exit_gitpal()

# System Exit
def exit_gitpal():
    print("\nExiting GitPal.\n")
    sys.exit()

# Main Menu
def main_menu():
    while True:
        print("\n================================")
        print("       Welcome to GitPal")
        print("================================")
        print("[1] Repository Status")
        print("[2] Stage Changes")
        print("[3] Commit Changes")
        print("[4] Push Changes")
        print("[5] Remote Repository")
        print("[6] Exit")
        print("================================")

        user_choice = input("Select an option: ")

        if user_choice == "1":

            repo_status = get_repository_status()
            check_file_directory()

            if repo_status is None:
                color_text("\nFailed to retrieve repository status.", "red")

            elif not repo_status:
                color_text("\nWorking tree is clean.", "green")

            else:
                print("\nRepository Changes:")

                for item in repo_status:
                    color_text(f"{item['status']}: {item['file']}", item['color'])

            return_to_menu()

        elif user_choice == "2":

            status = get_repository_status()

            if status is None:
                color_text("\nFailed to retrieve repository status.", "red")

            elif not status:
                color_text("\nThere are no changes to stage.", "yellow")
                color_text("Please add a file or make a change before staging", "yellow")

            else:
                staged_status = git_add_stages()
                
                if staged_status is not None:
                    color_text("\nSuccessfully staged changes\n", "green")

                    for item in staged_status:
                        color_text(f"{item['status']}: {item['file']}", item['color'])

                    return_to_menu()

                else:
                    color_text("\nFailed to stage changes.", "red")

        elif user_choice == "3":

            staged_changes = has_staged_changes()

            if staged_changes is None:
                color_text("\nFailed to retrieve repository status.", "red")

            elif not staged_changes:
                color_text("\nThere are no staged changes to commit.", "yellow")
                color_text("Please make a change and stage it before committing.", "yellow")

                return_to_menu()

            else:
                commit_message = input("\nEnter commit message: ")

                if stages_changes(commit_message):
                    color_text("\nSuccessfully committed changes.", "green")

                    return_to_menu()

                else:
                    color_text("\nFailed to commit changes.", "red")

        elif user_choice == "4":

            push_results = git_push_changes()

            if push_results is True:
                color_text("\nSuccessfully pushed changes.", "green")

                return_to_menu()   

            else:
                color_text("\nAttention: Push failed.", "red")

                color_text("\nGit Error:", "red")
                print(push_results["error"])

                print("\nWhy this happened:")
                print(push_results["explanation"])

                color_text("\nRecommended action:", "yellow")
                print(push_results['recommended'])

                return_to_menu()

        elif user_choice == "5":
            remote_repository()

        elif user_choice == "6":
            exit_gitpal()

        else:
            print("\nInvalid option. Please try again.")


# Main program execution
def main():

    # ==========================================
    # 1. CHECK GITHUB AUTHENTICATION
    # ==========================================

    loading_screen("Checking Github authentication: ")

    if is_github_authenticated():
        color_text("GitHub account is already authenticated.\n", "green")

    else:
        color_text("GitHub authentication failed.", "yellow")

        user_auth_answer = input(
            "Do you want to authenticate with GitHub? [y/n]: "
        )

        if user_auth_answer.lower() == 'y':

            if authenticate_github():
                color_text("Successfully authenticated with GitHub.\n", "green")

            else:
                print("GitHub authentication canceled.")
                exit_gitpal()

        else:
            print("GitHub authentication canceled.")
            exit_gitpal()


    # ==========================================
    # 2. CHECK LOCAL GIT REPOSITORY
    # ==========================================

    loading_screen("Checking Git repository: ")

    if is_git_repository():
        color_text("This is a Git repository.\n", "green")

    else:
        color_text("This is not a Git repository.", "red")

        user_answer = input(
            "Do you want to initialize a new Git repository here? [y/n]: "
        )

        if user_answer.lower() == 'y':

            # Run the git command 'git init'
            init_git_repo = subprocess.run(
                ['git', 'init'],
                capture_output=True,
                text=True
            )

            if init_git_repo.returncode == 0:
                color_text("\nSuccessfully initialized a new Git repository.", "green")

                # Check if the repository is now initialized
                if is_git_repository():
                    print("\nThis is now a Git repository.\n")
                else:
                    color_text("Failed to verify the Git repository initialization.\n", "red")

            else:
                color_text("\nFailed to initialize a Git repository.", "red")
                color_text("\nGit Error:", "red")
                print(init_git_repo.stderr)

        else:
            print("\nGit repository initialization canceled.")
            exit_gitpal()

    # ==========================================
    # 3. CHECK GIT REMOTE
    # ==========================================

    if has_git_remote():

        loading_screen("Checking remote repository: ")

        color_text("This Git repository is connected to a remote repository.", "green")
    else:
        color_text("This Git repository is not connected to any remote repository.", "red")

        user_input = input("Do you want to connect this into an existing remote repository? [y/n]: ")

        if user_input.lower() == 'y':
            remote_origin_input = input("\nPaste your remote origin repository link here: ")

            print()
            loading_screen("Verifying the remote repository: ")

            if verify_git_remote(remote_origin_input):

                if git_remote_origin(remote_origin_input):
                    color_text("Successfully connected to the remote repository.", "green")

                else:
                    color_text("Failed to connect to the remote repository", "red")

            else:
                color_text("The GitHub repository could not be found or accessed.", "yellow")
                color_text("Please check the repository URL and your GitHub permissions.", "yellow")

                time.sleep(3)


        else:
            print("\nRemote repository connection canceled.")


    # ==========================================
    # 4. MAIN MENU
    # ==========================================

    main_menu()

if __name__ == "__main__":
    main()
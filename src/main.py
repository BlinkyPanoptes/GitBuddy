import subprocess
from git_auth import is_github_authenticated, authenticate_github
from git_remote import has_git_remote, git_remote_origin
from git_operations import get_repository_status, git_add_stages, stages_changes, git_push_changes, has_staged_changes, is_git_repository
from file_operations import check_file_directory
import sys

# Main Menu
def main_menu():
    while True:
        print("\n================================")
        print("           GitBuddy")
        print("================================")
        print("1. Repository Status")
        print("2. Stage Changes")
        print("3. Commit Changes")
        print("4. Push Changes")
        print("5. Exit")
        print("================================")

        user_choice = input("Select an option: ")

        if user_choice == "1":

            repo_status = get_repository_status()
            check_file_directory()

            if repo_status is None:
                print("Failed to retrieve repository status.")

            elif not repo_status:
                print("Working tree is clean.")

            else:
                print("\nRepository Changes:")

                for item in repo_status:
                    print(f"{item['status']}: {item['file']}")

            user_input = input("\nBack to Main Menu?(y/n): ")

            if user_input.lower() != 'y':
                print("Exiting GitBuddy.")
                sys.exit()

        elif user_choice == "2":

            status = get_repository_status()

            if status is None:
                print("Failed to retrieve repository status.")

            elif not status:
                print("There are no changes to stage.")
                print("Please add a file or make a change before staging")

                user_input = input("\nBack to Main Menu?(y/n): ")

                if user_input.lower() != 'y':
                    print("Exiting GitBuddy.")
                    sys.exit()

            else:

                staged_status = git_add_stages()
                
                if staged_status is not None:
                    print("\nSuccessfully staged changes\n")

                    for item in staged_status:
                        print(f"{item['status']}: {item['file']}")

                    user_input = input("\nBack to Main Menu?(y/n): ")

                    if user_input.lower() != 'y':
                        print("Exiting GitBuddy.")
                        sys.exit()

                else:
                    print("Failed to stage changes.")

        elif user_choice == "3":

            staged_changes = has_staged_changes()

            if staged_changes is None:
                print("Failed to retrieve repository status.")

            elif not staged_changes:
                print("There are no staged changes to commit.")
                print("Please make a change and stage it before committing.")

                user_input = input("\nBack to Main Menu?(y/n): ")
                
                if user_input.lower() != 'y':
                    print("Exiting GitBuddy.")
                    sys.exit()

            else:
                commit_message = input("Enter commit message: ")

                if stages_changes(commit_message):
                    print("Successfully committed changes.")

                    user_input = input("\nBack to Main Menu?(y/n): ")
                    
                    if user_input.lower() != 'y':
                        print("Exiting GitBuddy.")
                        sys.exit()
                else:
                    print("Failed to commit changes.")

        elif user_choice == "4":

            push_results = git_push_changes()

            if push_results is True:
                print("Successfully pushed changes.")

                user_input = input("\nBack to Main Menu?(y/n): ")

                if user_input.lower() != 'y':
                    print("Exiting GitBuddy.")
                    sys.exit()   
            else:
                print("\nAttention: Push failed.")

                print("\nGit Error:")
                print(push_results["error"])

                print("\nWhy this happened:")
                print(push_results["explanation"])

                print("\nRecommended action:")
                print(push_results['recommended'])

                user_input = input("\nBack to Main Menu?(y/n): ")

                if user_input.lower() != 'y':
                    print("Exiting GitBuddy.")
                    sys.exit()

        elif user_choice == "5":
            print("Exiting GitBuddy.")
            sys.exit()

        else:
            print("Invalid option. Please try again.")


# Main program execution
def main():

    # ==========================================
    # 1. CHECK GITHUB AUTHENTICATION
    # ==========================================

    if is_github_authenticated():
        print("\nGitHub account is already authenticated.")

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

if __name__ == "__main__":
    main()
import subprocess
from error_handler import handle_git_error

# This function checks if the current directory is a Git repository
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

def get_git_status():
    check_git_status = subprocess.run(['git', 'status', '--short',], capture_output = True, text = True)

    if check_git_status.returncode == 0:
        return check_git_status.stdout
    else:
        return False

def parse_git_status(status_output):
    # Store the parsed Git status information
    status_list = []

    # Process each line returned by git status
    for line in status_output.splitlines():

        # Get the Git status code and file name
        status_code = line[:2]
        file_name = line[3:]

        # Determine the status
        if status_code == '??':
            status = 'untracked'

        elif status_code[0] == 'M':
            status = 'staged modification'

        elif status_code[1] == 'M':
            status = 'modified'

        elif status_code[0] == 'A':
            status = 'staged addition'

        elif status_code[0] == 'D':
            status = 'staged deletion'

        elif status_code[1] == 'D':
            status = 'deleted'

        else:
            status = 'other'

        status_list.append({
            'status': status,
            'file': file_name
        })

    return status_list

# This function is getting the raw data of a the status of the repository
def get_repository_status():
    raw_status = get_git_status()

    if raw_status is None:
        return None

    return parse_git_status(raw_status)

# This function is to check if there are staged changes
def has_staged_changes():
    status = get_repository_status()

    if status is None:
        return None

    for item in status:
        if item['status'] == 'staged modification':
            return True

        elif item['status'] == 'staged addition':
            return True

        elif item['status'] == 'staged deletion':
            return True

    return False

# This function is the git add
def git_add_stages():
    stage_results = subprocess.run(['git', 'add', '.'], capture_output = True, text = True)

    if stage_results.returncode == 0:

        status = get_repository_status()
        staged_files = []

        for item in status:

            if item['status'] == 'staged modification':
                staged_files.append(item)

            elif item['status'] == 'staged addition':
                staged_files.append(item)

            elif item['status'] == 'staged deletion':
                staged_files.append(item)

        return staged_files
    else:
        return None

# This function is the git commit -m
def stages_changes(message):
    commit_results = subprocess.run(
        ['git', 'commit', '-m', message],
        capture_output=True,
        text=True
    )

    if commit_results.returncode == 0:
        return True
    else:
        return False

# This function is the git push
def git_push_changes():
    push_results = subprocess.run(['git', 'push', '-u', 'origin', 'HEAD'], capture_output = True, text = True)

    if push_results.returncode == 0:
        return True
    return handle_git_error(push_results.stderr.strip())
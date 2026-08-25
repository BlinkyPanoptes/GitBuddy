import subprocess

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
        False

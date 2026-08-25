import subprocess

def is_github_authenticated():
    # Check the current GitHub authentication status
    check_github_auth = subprocess.run(
        ['gh', 'auth', 'status'],
        capture_output=True,
        text=True
    )

    # Check if GitHub CLI reports an authenticated account
    if "Logged in to github.com" in check_github_auth.stdout:
        return True
    else:
        return False

def authenticate_github():
    # Start the GitHub CLI authentication process
    auth_login = subprocess.run(['gh', 'auth', 'login'])

    if auth_login.returncode == 0:
        return True
    else:
        return False
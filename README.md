# GitPal

A pal for your daily Git needs.

## Requirements

- Python 3.10 or later
- [Git](https://git-scm.com/downloads)
- [GitHub CLI (`gh`)](https://cli.github.com/), used for GitHub authentication and remote repository verification
- [pipx](https://pipx.pypa.io/) (recommended) for installing GitPal as a standalone command

## Installation

GitPal is a CLI tool, so it's meant to be installed once and run from anywhere — not activated inside a project's virtual environment.

### Option 1: pipx (recommended)

[pipx](https://pipx.pypa.io/) installs GitPal into its own isolated environment and puts the `gitpal` command on your `PATH`, so it works in any directory without you ever needing to create or activate a venv.

```bash
# Install pipx if you don't already have it
python -m pip install --user pipx
python -m pipx ensurepath

# Clone and install GitPal
git clone https://github.com/BlinkyPanoptes/GitPal.git
cd GitPal
pipx install .
```

After installation, restart your terminal (so the updated `PATH` takes effect) and run:

```bash
gitpal
```

### Option 2: pip (in a virtual environment)

If you'd rather manage the environment yourself:

```bash
git clone https://github.com/BlinkyPanoptes/GitPal.git
cd GitPal
python -m venv .venv
.venv\Scripts\activate   # on Windows
source .venv/bin/activate # on macOS/Linux

pip install .
gitpal
```

### Updating

```bash
cd GitPal
git pull
pipx reinstall gitpal   # or: pip install --upgrade . (Option 2)
```

## Usage

Run `gitpal` from inside the local Git repository you want to work with:

```bash
cd path/to/your/project
gitpal
```

On first run, GitPal walks you through setup:

1. **GitHub authentication** — checks whether you're logged in via GitHub CLI, and offers to run `gh auth login` if not.
2. **Local repository check** — detects whether the current directory is a Git repository, and offers to run `git init` if it isn't.
3. **Remote check** — detects whether a remote is configured, and lets you connect one by pasting a repository URL.

Once setup is complete, you land on the main menu:

```text
                Welcome to GitPal
 Option  Action
 1       Repository Status
 2       Stage Changes
 3       Commit Changes
 4       Push Changes
 5       Remote Repository
 6       Exit
```

From here you can:

- **Repository Status** — view untracked, modified, and staged files at a glance
- **Stage Changes** — stage everything (`git add .`) or pick specific files
- **Commit Changes** — review what's staged, confirm, and enter a commit message
- **Push Changes** — push to the configured remote, with plain-language explanations if it fails
- **Remote Repository** — view or change the configured `origin` remote
- **Exit** — quit GitPal

## Current Version

**v0.3.0 — Packaged CLI Release**

GitPal is a terminal-based Git and GitHub assistant built with Python. It is currently in early development.

Version 0.3.0 expands GitPal from a startup and repository configuration tool into a functional Git workflow assistant. It introduces repository status monitoring, directory inspection, staging, committing, pushing, remote repository management, Git error handling, loading animations, and colorized terminal output through an interactive command-line interface. It also packages GitPal as an installable CLI tool, so it runs via a standalone `gitpal` command instead of requiring a project virtual environment.

## Current Features

### GitHub Authentication

- Detect whether the user is authenticated with GitHub
- Authenticate through GitHub CLI when necessary
- Reuse an existing GitHub authentication session
- Support first-time GitHub authentication

### Local Git Repository

- Detect whether the current directory is a Git repository
- Ask the user whether to initialize Git when necessary
- Initialize a repository using `git init`
- Verify that the repository was successfully initialized

### Git Remote

- Detect whether the local repository has a configured remote
- Inform the user when no remote is configured
- Connect the local repository to an existing remote repository
- Verify that the remote GitHub repository exists and is accessible
- Configure the remote as `origin`
- View the current remote repository
- Change the configured remote repository
- Prevent invalid or inaccessible repositories from being configured as the remote

### Repository Status

- Retrieve the current Git repository status
- Parse Git status codes
- Identify untracked files
- Identify modified files
- Identify staged modifications
- Identify staged additions
- Identify staged deletions
- Detect when the working tree is clean
- Display status information using color-coded output

### Directory Inspection

- Display files and directories contained within the current repository
- Exclude the `.git` directory from displayed contents
- Warn the user when a repository contains no project files

### Git Operations

- Stage changes using `git add .`
- Display files successfully staged
- Validate that changes exist before staging
- Validate that staged changes exist before committing
- Commit changes using a user-provided commit message
- Push changes to the configured remote repository
- Automatically establish upstream tracking during the first push

### Git Error Handling

- Capture errors returned by Git operations
- Display the original Git error
- Provide a human-readable explanation for recognized Git errors
- Provide recommended actions when a recognized error occurs
- Provide a generic explanation for unrecognized Git errors

### Terminal UI

GitPal is designed around a terminal-first workflow rather than a separate graphical interface.

Current UI features include:

- Loading animations for repository checks and operations
- Colorized terminal output
- Green output for successful operations
- Yellow output for instructions and actions requiring attention
- Red output for errors and failures
- White (default) output for neutral, informational messages
- Structured interactive menus
- Dedicated UI modules for terminal presentation

See the [Usage](#usage) section above for a look at the main menu.
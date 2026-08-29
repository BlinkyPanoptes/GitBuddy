# GitPal

A pal for your daily Git needs.

## Current Version

**v0.2.0 — Core Git Workflow**

GitPal is a terminal-based Git and GitHub assistant built with Python. It is currently in early development.

Version 0.2.0 expands GitPal from a startup and repository configuration tool into a functional Git workflow assistant. It introduces repository status monitoring, directory inspection, staging, committing, pushing, remote repository management, Git error handling, loading animations, and colorized terminal output through an interactive command-line interface.

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
- Yellow output for warnings and actions requiring attention
- Red output for errors and failures
- Cyan output for informational messages
- Structured interactive menus
- Dedicated UI modules for terminal presentation

GitPal currently provides the following main menu:

```text
================================
       Welcome to GitPal
================================
[1] Repository Status
[2] Stage Changes
[3] Commit Changes
[4] Push Changes
[5] Remote Repository
[6] Exit
================================
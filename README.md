# GitBuddy

A simple terminal-based Git and GitHub assistant built with Python.

## Current Version

**v0.2.0 — Core Git Workflow**

GitBuddy is currently in early development.

Version 0.2.0 expands GitBuddy from a startup and repository configuration tool into a functional Git workflow assistant. It introduces repository status monitoring, staging, committing, and pushing changes through an interactive terminal interface.

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
- Configure the remote as `origin`

### Repository Status

- Retrieve the current Git repository status
- Parse Git status codes
- Identify untracked files
- Identify modified files
- Identify staged modifications
- Identify staged additions
- Identify staged deletions
- Detect when the working tree is clean

### Git Operations

- Stage changes using `git add .`
- Validate that changes exist before staging
- Validate that staged changes exist before committing
- Commit changes using a user-provided commit message
- Push changes to the configured remote repository
- Automatically establish upstream tracking during the first push

### Interactive Terminal Menu

GitBuddy currently provides the following menu:

```text
================================
           GitBuddy
================================
1. Repository Status
2. Stage Changes
3. Commit Changes
4. Push Changes
5. Exit
================================
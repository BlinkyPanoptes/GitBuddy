# GitBuddy

A simple terminal-based Git and GitHub assistant built with Python.

## Current Version

**v0.1 — Startup Workflow**

GitBuddy is currently in early development. Version 0.1 focuses on establishing and testing the application's startup workflow, GitHub authentication, local Git repository management, and remote repository configuration.

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

## Current Startup Workflow

GitBuddy currently follows this startup sequence:

```text
GitHub Authentication
        ↓
Local Git Repository Check
        ↓
Git Remote Check
        ↓
Project Ready

TESTING
# Agent Instructions

This project uses **bd** (beads) for issue tracking. Run `bd onboard` to get started.

## Shell Environment

**This project uses xonsh shell, NOT bash.**

- **Multiline strings**: Use triple quotes `"""multiline string"""`
- **String arguments**: Use quotes around arguments with special chars
- **No backslash escaping**: Use quotes instead of `\`

## Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --status in_progress  # Claim work
bd close <id>         # Complete work
bd sync               # Sync with git
```

### Creating Issues with Multiline Descriptions

```xonsh
bd create --title "Issue title" --description """
Multiline description here
- Point 1
- Point 2
""" --label "priority:high"

# With dependencies
bd create --title "Subtask" --description "Details" --deps "parent-id"

# Multiple dependencies
bd create --title "Task" --deps "id1,blocks:id2"
```

## Git Push Policy

**CRITICAL: NEVER push to remote without explicit user permission.**

- **ALWAYS ask** before running `git push`
- Commit locally, show status, then ASK: "Ready to push?"
- Only push when user explicitly says: "push", "commit and push", "deploy", etc.
- Exception: "Landing the plane" workflow at session end (see below)

## Landing the Plane (Session Completion)

**When ending a work session**, you MUST complete ALL steps below. Work is NOT complete until `git push` succeeds.

**MANDATORY WORKFLOW:**

1. **File issues for remaining work** - Create issues for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **ASK PERMISSION TO PUSH** - Then execute:
   ```bash
   git pull --rebase
   bd sync
   git push
   git status  # MUST show "up to date with origin"
   ```
5. **Clean up** - Clear stashes, prune remote branches
6. **Verify** - All changes committed AND pushed
7. **Hand off** - Provide context for next session

**CRITICAL RULES:**
- NEVER push without explicit user permission
- Commits are local until user approves push
- If user says "don't push" or "stop", commit locally and stop
- Only push during session completion if user approves

## Deployment

This site uses dual deployment strategy:

### Primary/Canonical: Swarm (Manual)
- **Deployment**: `just deploy-all` 
- **Prerequisites**: Bee node running, environment variables configured
- **Identity**: owencampbell-website
- **Gateways**: owencampbell.eth.limo, owencampbell.eth.link, owencampbell.bzz.link

### Secondary/Backup: GitHub Pages (Automated)
- **Trigger**: Push to main branch
- **Method**: Artifact-based deployment
- **Workflow**: .github/workflows/gh-pages.yml

## Environment Setup

Required environment variables (create .env file):
- `SWARM_BATCH_ID`: Batch ID from your bee node
- `SWARM_FEED_MANIFEST`: Generated after first upload

## Swarm Deployment Commands

```bash
just build          # Build Hugo site
just deploy         # Upload to Swarm
just verify         # Test deployment
just status         # Check Swarm status
just deploy-all     # Full workflow (build + deploy + verify)
```

## Initial Setup

1. Configure bee node and create batch ID using swarm-cli directly
2. Copy `.env.example` to `.env` and add Swarm variables
3. Run `just deploy-all` for initial deployment


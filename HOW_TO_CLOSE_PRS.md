# How to Close Pull Requests

This guide provides step-by-step instructions for closing the abandoned pull requests identified in [PULL_REQUEST_STATUS.md](PULL_REQUEST_STATUS.md).

## PRs Recommended for Closure

Based on the analysis in PULL_REQUEST_STATUS.md, the following PRs should be closed:

- **PR #3**: Investigate thermodynamic conditions for intelligence emergence
- **PR #4**: Investigate minimal thermodynamic conditions for intelligence emergence  
- **PR #5**: Explore minimal thermodynamic conditions for intelligence emergence
- **PR #6**: Investigate thermodynamic conditions for intelligence emergence
- **PR #7**: Explore minimal thermodynamic conditions for intelligence emergence
- **PR #8**: Explore minimal thermodynamic conditions for emerging intelligence
- **PR #9**: Investigate minimal thermodynamic conditions for intelligence

**Reason for closure:** All these PRs are draft PRs with no code changes (0 additions, 0 deletions, 0 changed files) and appear to have been superseded by the successfully merged PR #10.

## Method 1: Using GitHub Web Interface (Recommended for Manual Closure)

### Steps:

1. **Navigate to the Pull Request**
   - Go to: https://github.com/vanj900/Thermo-AI/pulls
   - Click on the PR you want to close (e.g., PR #3)

2. **Close the Pull Request**
   - Scroll to the bottom of the PR page
   - Click the **"Close pull request"** button
   - Optionally, add a comment explaining why you're closing it:
     ```
     Closing this PR as it was a draft with no code changes and its objectives 
     were completed by PR #10 which successfully documented the minimal 
     thermodynamic conditions for intelligence emergence.
     ```

3. **Repeat for Each PR**
   - Repeat steps 1-2 for PRs #3, #4, #5, #6, #7, #8, and #9

### Visual Guide:

```
PR Page → Scroll to bottom → [Close pull request] button → (Optional) Add comment → Confirm
```

## Method 2: Using GitHub CLI (For Batch Closure)

If you have the GitHub CLI (`gh`) installed, you can close PRs from the command line.

### Prerequisites:

```bash
# Install GitHub CLI (if not already installed)
# For Ubuntu/Debian:
# sudo apt install gh

# For macOS:
# brew install gh

# Authenticate (if not already done)
gh auth login
```

### Close a Single PR:

```bash
# Close PR with a comment
gh pr close 3 --repo vanj900/Thermo-AI --comment "Closing as draft with no changes, superseded by PR #10"

# Close PR without comment
gh pr close 3 --repo vanj900/Thermo-AI
```

### Close Multiple PRs (Batch Script):

```bash
#!/bin/bash
# Save this as close_abandoned_prs.sh

REPO="vanj900/Thermo-AI"
COMMENT="Closing this draft PR with no code changes. Its objectives were completed by the successfully merged PR #10 which documented minimal thermodynamic conditions for intelligence emergence."

# Array of PR numbers to close
PRS=(3 4 5 6 7 8 9)

for pr in "${PRS[@]}"; do
    echo "Closing PR #$pr..."
    gh pr close $pr --repo $REPO --comment "$COMMENT"
    echo "PR #$pr closed successfully"
    echo "---"
done

echo "All abandoned PRs have been closed!"
```

**To use the script:**

```bash
# Make it executable
chmod +x close_abandoned_prs.sh

# Run it
./close_abandoned_prs.sh
```

## Method 3: Using GitHub API (Advanced)

If you prefer using the GitHub API directly with `curl`:

```bash
# Set your GitHub token
GITHUB_TOKEN="your_github_token_here"
REPO_OWNER="vanj900"
REPO_NAME="Thermo-AI"

# Close a single PR (e.g., PR #3)
curl -X PATCH \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/pulls/3 \
  -d '{"state":"closed"}'
```

## What Happens When You Close a PR?

- ✅ The PR is marked as "Closed" (not merged)
- ✅ The PR remains in the repository history
- ✅ The branch associated with the PR is **not** automatically deleted
- ✅ The PR can be reopened later if needed
- ❌ No code changes are merged into the main branch

## Optional: Delete Branches After Closing

After closing the PRs, you may want to delete their associated branches to keep the repository clean:

### Using GitHub Web Interface:

1. Go to: https://github.com/vanj900/Thermo-AI/branches
2. Find the branch (e.g., `copilot/research-minimal-thermodynamic-conditions`)
3. Click the trash icon to delete it

### Using GitHub CLI:

```bash
# List all branches
gh api repos/vanj900/Thermo-AI/branches --paginate | jq -r '.[].name'

# Delete a specific branch (remote)
git push origin --delete copilot/research-minimal-thermodynamic-conditions

# Or using gh CLI
gh api -X DELETE repos/vanj900/Thermo-AI/git/refs/heads/copilot/research-minimal-thermodynamic-conditions
```

## Verification

After closing PRs, verify the changes:

### Check Open PRs:

```bash
# Using gh CLI
gh pr list --repo vanj900/Thermo-AI --state open

# Or visit: https://github.com/vanj900/Thermo-AI/pulls
```

### Check Closed PRs:

```bash
# Using gh CLI  
gh pr list --repo vanj900/Thermo-AI --state closed

# Or visit: https://github.com/vanj900/Thermo-AI/pulls?q=is%3Apr+is%3Aclosed
```

## Summary of Actions

| PR # | Status | Action | Branch to Delete (Optional) |
|------|--------|--------|----------------------------|
| #3 | Open (Draft) | Close | `copilot/explore-intelligence-thermodynamics` |
| #4 | Open (Draft) | Close | `copilot/investigate-minimal-intelligence-conditions` |
| #5 | Open (Draft) | Close | `copilot/explore-thermodynamic-intelligence` |
| #6 | Open (Draft) | Close | `copilot/investigate-intelligence-thermodynamics` |
| #7 | Open (Draft) | Close | `copilot/discuss-thermodynamics-intelligence` |
| #8 | Open (Draft) | Close | `copilot/discuss-intelligence-emergence` |
| #9 | Open (Draft) | Close | `copilot/research-minimal-thermodynamic-conditions` |

## Recommended Closure Comment Template

When closing each PR, consider adding a comment like:

```
Closing this draft PR as it has no code changes and its objectives have been 
completed by PR #10, which successfully merged documentation of minimal 
thermodynamic conditions for intelligence emergence.

See PULL_REQUEST_STATUS.md for a comprehensive analysis of all PRs in this 
repository.
```

## After Closing All PRs

Once all abandoned PRs are closed:

1. Update [PULL_REQUEST_STATUS.md](PULL_REQUEST_STATUS.md) to reflect the new status
2. The repository will have a cleaner PR list showing only active/relevant work
3. New contributors will have less confusion about what work is actually in progress

## Need Help?

- **GitHub Docs on Closing PRs**: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/closing-a-pull-request
- **GitHub CLI Docs**: https://cli.github.com/manual/gh_pr_close
- **Questions?**: Open a new issue in the repository

---

**Note**: Make sure you have the necessary permissions (write access) to close PRs in the repository. Only repository collaborators, maintainers, or owners can close pull requests.

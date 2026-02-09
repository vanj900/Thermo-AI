# Quick Reference: Closing Pull Requests

## TL;DR - Fastest Methods

### Method 1: GitHub Web (Easiest)
1. Go to https://github.com/vanj900/Thermo-AI/pulls
2. Click on a PR (e.g., #3)
3. Scroll down and click **"Close pull request"**
4. Repeat for PRs #3, #4, #5, #6, #7, #8, #9

### Method 2: GitHub CLI (Fastest for Multiple PRs)
```bash
# Close single PR
gh pr close 3 --repo vanj900/Thermo-AI

# Close all abandoned PRs with one command
for pr in 3 4 5 6 7 8 9; do gh pr close $pr --repo vanj900/Thermo-AI; done
```

### Method 3: Use Our Script (Safest)
```bash
./scripts/close_abandoned_prs.sh
```

## PRs to Close
- PR #3, #4, #5, #6, #7, #8, #9 (all drafts with 0 changes)

## Why Close Them?
These are abandoned drafts with no code. Their work was completed by PR #10.

## Full Guide
See [HOW_TO_CLOSE_PRS.md](HOW_TO_CLOSE_PRS.md) for complete instructions.

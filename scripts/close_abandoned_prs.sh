#!/bin/bash

# Script to close abandoned pull requests in vanj900/Thermo-AI repository
# These PRs are drafts with no code changes, superseded by PR #10

set -e  # Exit on error

REPO="vanj900/Thermo-AI"
COMMENT="Closing this draft PR with no code changes. Its objectives were completed by the successfully merged PR #10 which documented minimal thermodynamic conditions for intelligence emergence. See PULL_REQUEST_STATUS.md for details."

# Array of PR numbers to close
PRS=(3 4 5 6 7 8 9)

echo "=========================================="
echo "PR Closure Script for Thermo-AI"
echo "=========================================="
echo ""
echo "This script will close the following abandoned PRs:"
for pr in "${PRS[@]}"; do
    echo "  - PR #$pr"
done
echo ""
echo "Repository: $REPO"
echo ""

# Check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo "❌ ERROR: GitHub CLI (gh) is not installed."
    echo ""
    echo "Please install it first:"
    echo "  - Ubuntu/Debian: sudo apt install gh"
    echo "  - macOS: brew install gh"
    echo "  - Windows: winget install GitHub.cli"
    echo ""
    echo "Or visit: https://cli.github.com/manual/installation"
    exit 1
fi

# Check if authenticated
if ! gh auth status &> /dev/null; then
    echo "❌ ERROR: Not authenticated with GitHub CLI."
    echo ""
    echo "Please run: gh auth login"
    exit 1
fi

echo "✅ GitHub CLI is installed and authenticated"
echo ""

# Confirm before proceeding
read -p "Do you want to proceed with closing these PRs? (yes/no): " confirmation

if [[ "$confirmation" != "yes" ]]; then
    echo ""
    echo "❌ Operation cancelled by user."
    exit 0
fi

echo ""
echo "=========================================="
echo "Starting PR closure process..."
echo "=========================================="
echo ""

# Close each PR
success_count=0
failed_count=0

for pr in "${PRS[@]}"; do
    echo "Processing PR #$pr..."
    
    if gh pr close $pr --repo $REPO --comment "$COMMENT" 2>/dev/null; then
        echo "✅ PR #$pr closed successfully"
        ((success_count++))
    else
        echo "❌ Failed to close PR #$pr (it may already be closed or you lack permissions)"
        ((failed_count++))
    fi
    
    echo "---"
    sleep 1  # Rate limiting courtesy
done

echo ""
echo "=========================================="
echo "Summary"
echo "=========================================="
echo "✅ Successfully closed: $success_count PRs"
echo "❌ Failed to close: $failed_count PRs"
echo ""

if [ $success_count -eq ${#PRS[@]} ]; then
    echo "🎉 All abandoned PRs have been closed successfully!"
    echo ""
    echo "Next steps:"
    echo "  1. Verify closures at: https://github.com/$REPO/pulls?q=is%3Apr+is%3Aclosed"
    echo "  2. Optionally delete the associated branches"
    echo "  3. Update PULL_REQUEST_STATUS.md to reflect the closures"
else
    echo "⚠️  Some PRs could not be closed. Please check manually."
    echo ""
    echo "Common reasons for failure:"
    echo "  - PR is already closed"
    echo "  - Insufficient permissions"
    echo "  - Network issues"
    echo ""
    echo "You can close PRs manually at: https://github.com/$REPO/pulls"
fi

echo ""
echo "=========================================="

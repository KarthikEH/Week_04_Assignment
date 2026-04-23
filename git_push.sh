#!/bin/bash
git remote set-url origin https://github.com/KarthikEH/Week4_02_ui_assistant.git

echo "Staging all Assignment folders..."
# This adds the folders AND everything inside them in one go
git add wk4_assignment_01/ wk4_assignment_02/ wk4_assignment_03/ wk4_assignment_04/ wk4_assignment_05/
git add git_push.sh .gitignore

echo "Committing..."
git commit -m "Organized Week 4 into structured assignment folders"

echo "Pushing to GitHub..."
git push origin main
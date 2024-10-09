#!/bin/bash

echo "Loading the new and modified Markdown files in the articles folder"

# Find new or modified markdown files in the articles folder using git diff with ACM filter
FILES=$(git diff --name-only --diff-filter=ACM HEAD origin/main -- "articles/*.md")

# Check if any files were found
if [ -z "$FILES" ]; then
  echo "No new or modified markdown files found."
  exit 0
fi

# Loop through the found files and run validation
for x in $FILES; do
  # Call the Python script to validate the file and store the result
  is_valid_md=$(python validate_markdown_metadata.py $x)

  # If the result is "True", the file is valid, continue processing
  if [[ $is_valid_md == "True" ]]; then
    echo "Validating file $x"
  else
    echo "File $x failed"
    exit 1
  fi
done
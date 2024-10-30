#!/bin/bash

echo "Searching new and modified Markdown files in the articles folder"

# Find new or modified markdown files in the articles folder using git diff with ACM filter
FILES=$(git diff --name-only --diff-filter=ACM origin/main..HEAD -- "articles/*.md")

echo

# Check if any files were found
if [ -z "$FILES" ]; then
  echo "No new or modified markdown files found."
  exit 0
  else
    echo "Detected files:"
    for file in $FILES; do
      echo "- $file"
    done
fi

echo

# Initialize arrays to store validations results
passed_files=()
failed_files=()

# Loop through the found files and run validation
for x in $FILES; do
  # Call the Python script to validate the file and store the result
  is_valid_md=$(python validate_markdown_metadata.py $x)

  # Check validation and store in respective array
  if [[ $is_valid_md == "True" ]]; then
    passed_files+=("$x")
  else
    failed_files+=("$x")
  fi
done

echo "Validation results"
echo

# Display validation results
if [ ${#passed_files[@]} -gt 0 ]; then
  echo "Passed files:"
  for file in "${passed_files[@]}"; do
    echo "- $file"
  done
fi

echo 

if [ ${#failed_files[@]} -gt 0 ]; then
  echo "Failed files:"
  for file in "${failed_files[@]}"; do
    echo "- $file"
  done
fi

# Set the exit code based on whether there were any failed files
if [ ${#failed_files[@]} -gt 0 ]; then
  exit 1  # Exit with error code if any file failed
else
  echo "All files passed validation."
fi
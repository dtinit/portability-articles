#!/bin/bash

echo "Searching new and modified Markdown files in the articles folder"

# Find new or modified markdown files in the articles folder using git diff with ACM filter
FILES=$(git diff --name-only --diff-filter=ACM origin/main..HEAD -- "articles/*.md")

echo

# Check if any files were found
if [ -z "$FILES" ]; then
  echo "No new or modified articles found"
  exit 0
  else
    echo "Detected articles:"
    for file in $FILES; do
      echo "- $file"
    done
fi

echo

# Initialize arrays to store validations results
passed_articles=()
failed_articles=()
failed_messages=()

# Loop through the found articles and run validation
for x in $FILES; do
  # Call the Python script to validate the article and store the result
  validation_result=$(python validate_markdown_metadata.py "$x")

  # Check validation and store in respective array
  if [[ $validation_result == "True" ]]; then
    passed_articles+=("$x")
  else
    failed_articles+=("$x")
    # Store the error message
    failed_messages+=("$validation_result")
  fi
done

echo "Validation results"
echo

# Display validation results
if [ ${#passed_articles[@]} -gt 0 ]; then
  echo "Passed article(s):"
  for file in "${passed_articles[@]}"; do
    echo "- $file"
  done
  echo
fi 

if [ ${#failed_articles[@]} -gt 0 ]; then
  echo "Failed article(s):"
  for i in "${!failed_articles[@]}"; do
    echo "- ${failed_articles[$i]}"
    # Display each line of the error message
    echo " - ${failed_messages[$i]}" | sed 's/^/    /'
    echo
  done
fi

# Set the exit code based on whether there were any failed articles
if [ ${#failed_articles[@]} -gt 0 ]; then
  exit 1  # Exit with error code if any article failed
else
  echo "All articles passed validation."
fi
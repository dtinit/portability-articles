#!/bin/bash

echo "Loading the Markdown files that have changed"

for x in $(git diff --name-only HEAD origin/main -- "articles/*.md")
do
  is_valid_md=$(python validate_markdown_metadata.py $x)
  if [[ $is_valid_md == "True" ]]; then
    echo "Validating file $x"
  else
    echo "File $x failed"
    exit 1
  fi
done

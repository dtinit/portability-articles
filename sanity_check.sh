#!/bin/bash

echo "Loading the Markdown files that have changed"

for x in $(git diff --name-only origin/${GITHUB_HEAD_REF} main -- "*.md")
do
  is_valid_md=$(python validate_markdown_metadata.py $x)
  if $is_valid_md; then
    echo "Validating file $x"
  else
    echo "File $x failed"
    exit 1
  fi
done

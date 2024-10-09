import sys
import yaml
import re

# Helper method that ensures the file has both a starting and ending '---'
def has_yaml_header(file_content):
    """ Detects if a string (usually the contents of a .md file) has a YAML header
    >>> has_yaml_header("---\\nTest: Yes\\n---")
    True
    >>> has_yaml_header("Test: No")
    False
    >>> has_yaml_header("---\\nProblem: about to be too many dashes\\n----")
    False
    """
    p = re.compile(r"^---$", re.MULTILINE)
    results = p.findall(file_content)
    return len(results) > 1

# This method is extracted from Portmap
# and it should stay consistent with it if it needs updating
def extract_yaml_and_body(file_content):
    """ Extracts a YAML header delimited by lines consisting of '---' from the rest of a markdown document.
    >>> extract_yaml_and_body("---\\nTest: Data\\nPart: Deux\\n---\\nSeparate this body part\\n")
    ({'Test': 'Data', 'Part': 'Deux'}, 'Separate this body part\\n')
    """
    assert has_yaml_header(file_content) # File does not have a YAML header
    in_yaml_header = False
    in_body = False
    yaml_content = []
    body_content = []
    for line in file_content.split("\n"):
        if not in_yaml_header and not in_body and line == "---":
            in_yaml_header = True
        elif in_yaml_header and line == "---":
            in_yaml_header = False
            in_body = True
        elif in_yaml_header:
            yaml_content.append(line)
        elif in_body:
            body_content.append(line)

    yaml_content = yaml.safe_load('\n'.join(yaml_content))
    body = '\n'.join(body_content)
    return yaml_content, body

# Validates the required fields in the frontmatter
def validate_fields(frontmatter, file_path):

    # Validate 'title': Must be a string
    if not isinstance(frontmatter['title'], str):
        raise ValueError(f"'title' must be a string in {file_path}")

    # Validate 'datatype': Must be a string (no lists allowed)
    if not isinstance(frontmatter['datatype'], str):
        raise ValueError(f"'datatype' must be a string in {file_path}")

    # Validate 'sources'
    if isinstance(frontmatter['sources'], str):
        # Single source, valid
        pass
    elif isinstance(frontmatter['sources'], list):
        # Multiple sources, valid list format
        pass
    else:
        raise ValueError(f"'sources' must be either a string or a list in {file_path}")

    # Validate 'destinations'
    if isinstance(frontmatter['destinations'], str):
        # Single destination, valid
        pass
    elif isinstance(frontmatter['destinations'], list):
        # Multiple destinations, valid list format
        pass
    else:
        raise ValueError(f"'destinations' must be either a string or a list in {file_path}")
    
# Checks if a specified YAML field ends with a comma
def does_field_end_with_comma(field, yaml_body):
    datatype_pattern = re.compile(r"^" + re.escape(field) + r":\s*.*,\s*$", re.MULTILINE)
    match = datatype_pattern.search(yaml_body)
    return match is not None

def validate_frontmatter(file_path):
    try:
        # Open the markdown file and extract content
        with open(file_path, 'r') as f:
            # Reads content and stores it
            content = f.read()

            # Extract frontmatter and body using Portmap method
            frontmatter, _ = extract_yaml_and_body(content)
            
            # Validate the extracted frontmatter
            validate_fields(frontmatter, file_path)

            # Check for trailing commas
            fields_to_check = ['title', 'datatype', 'sources', 'destinations']
            # Iterate over fields to check and then check for trailing commas
            errors = [field for field in fields_to_check if does_field_end_with_comma(field, content)]

            # If there are any fields with trailing commas, raise an error
            if errors:
                raise ValueError(f"Trailing comma found in the following fields: {', '.join(errors)} in {file_path}")

            # If all validations pass, return "True"
            return "True"
    
    except yaml.YAMLError as e:
        # Catch any YAML syntax errors
        print(f"YAML Error in {file_path}: {e}")
        return "False"
    
    except Exception as e:
        # Catch other errors (missing fields, invalid structure, trailing comma, etc.)
        print(f"Error in {file_path}: {e}")
        return "False"

if __name__ == "__main__":
    # The script takes the file path as an argument
    file_path = sys.argv[1]
    # Run validation and print the result ("True" or "False")
    print(validate_frontmatter(file_path))
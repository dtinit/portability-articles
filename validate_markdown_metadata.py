import sys
import yaml
import re

# Helper function that checks if file content starts with a YAML header (---) before processing it
# Modify from Portmap
def has_yaml_header(file_content):
    return file_content.strip().startswith('---')

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

def validate_frontmatter(file_path):
    try:
        # Open the markdown file and extract content
        with open(file_path, 'r') as f:
            # Reads content and stores it
            content = f.read()

            # Extract frontmatter and body using Portmap method
            frontmatter, _ = extract_yaml_and_body(content)
            
            # Check if the parsed content is a dictionary (valid YAML structure)
            if not isinstance(frontmatter, dict):
                raise ValueError(f"Invalid frontmatter structure in {file_path}")

            # Define the required fields in the frontmatter
            required_fields = ['title', 'datatype', 'sources', 'destinations']
            
            # Check that all required fields are present
            for field in required_fields:
                if field not in frontmatter:
                    raise ValueError(f"Missing field '{field}' in {file_path}")

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

            # Now check for trailing commas in all fields in the original content
            # Using regex to match any fields that have a comma at the end of the line
            errors = []

            title_pattern = re.search(r'^title:\s*".*",\s*$', content[1], re.MULTILINE)
            if title_pattern:
                errors.append('title')

            datatype_pattern = re.search(r'^datatype:\s*".*",\s*$', content[1], re.MULTILINE)
            if datatype_pattern:
                errors.append('datatype')

            sources_pattern = re.search(r'^sources:\s*\[.*\],\s*$', content[1], re.MULTILINE)
            if sources_pattern:
                errors.append('sources')

            destinations_pattern = re.search(r'^destinations:\s*\[.*\],\s*$', content[1], re.MULTILINE)
            if destinations_pattern:
                errors.append('destinations')

            # If there are any errors, raise an error with the list of problematic fields
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
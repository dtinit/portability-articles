import sys
import yaml
import re

def validate_frontmatter(file_path):
    try:
        # Open the markdown file and extract content
        with open(file_path, 'r') as f:
            # Split the content by '---' which indicates YAML frontmatter in markdown
            content = f.read().split('---')
            
            # If there is no frontmatter section (should be between ---), raise an error
            if len(content) < 3:
                raise ValueError(f"No frontmatter found in {file_path}")
            
            # The actual YAML frontmatter is the second element (content[1])
            frontmatter = yaml.safe_load(content[1])
            
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
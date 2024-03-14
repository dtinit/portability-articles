from sys import argv

import frontmatter

KEYS = ['title', 'datatype', 'sources', 'destinations']

def article_validator(markdown_file):
  article = frontmatter.load(markdown_file)
  keys_indices = {key: index for index, key in enumerate(KEYS)}
  sorted_keys = sorted(list(article.keys()), key=lambda x: keys_indices.get(x, float('inf')))

  return True if sorted_keys == KEYS else False

def main():
  result = article_validator(argv[1])
  print(result)
  return result

if __name__ == "__main__":
    main()
    
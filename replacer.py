import sys
import re

def replace(text, find, replace):
    search = re.search(find, text, re.IGNORECASE)
    if search:
        found_text = search.group()
        if found_text.isupper():
            replace = replace.upper()
        elif found_text.istitle():
            replace = replace.title()
        else:
            replace = replace.lower()
    text = re.sub(find, replace, text, flags=re.IGNORECASE)
    return text

if __name__ == '__main__':
    for line in sys.stdin:
        line = line.strip()
        print replace(line, "neat", "lame")

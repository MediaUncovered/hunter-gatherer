import re

def remove_newlines(text):
    only_spaces = re.sub('(\s|\n|\r)', u" ", text)
    only_single_spaces = re.sub('(\s+)', u" ", only_spaces)
    return only_single_spaces.strip()

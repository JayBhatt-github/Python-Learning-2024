import re

# Define a regular expression pattern
pattern = "fox"

# Define a string
string = "The quick brown fox jumps over the lazy dog ."

# Use the re.search() function to search the string for the pattern
match = re.search(pattern, string)

# If a match is found, print the match
if match:
    print("Match found: ", match.group())
else:
    print("No match found.")

# Define a new regular expression pattern
pattern = "fox|dog"

# Use the re.findall() function to find all occurrences of the pattern in the string
matches = re.findall(pattern, string)

# Print all matches
print("All matches: ", matches)

# Find list of more meta characters here:
# https://regexr.com/
# https://www.ibm.com/docs/en/rational-clearquest/9.0.1?topic=tags-meta-characters-in-regular-expressions

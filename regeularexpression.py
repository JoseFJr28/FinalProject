import re

# Read file and get all lines
with open('animal-names.csv', 'r') as f:
    lines = f.readlines()

# Define regex pattern
pattern = r"^(?P<numbers>\d+),(?P<animals>\w.+)"

# Process lines
new_lines = []
for line in lines:
    new_line = re.sub(pattern, r'  \g<numbers>: "\g<animals>"', line.strip())
    new_lines.append(new_line)

# Write to new file
with open('new_file.txt', 'w') as f:
    for line in new_lines:
        f.write(line + ",\n")

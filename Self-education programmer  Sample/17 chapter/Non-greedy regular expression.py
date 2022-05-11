import re

t = "__one__ __two__ __there__"
found = re.findall("__.*?__", t)
for match in found:
    print(match)

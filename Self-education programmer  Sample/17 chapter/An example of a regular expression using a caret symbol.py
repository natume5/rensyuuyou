import re

zen = """Although never is
often better than
*right* now.
If the importantion
is hard to explain,
it's a bad idea.
If the implementation
is easy to explain,
it may be a good
idea. Namespaces
are one honking
great idea -- Let's
do more of those!"""


m = re.findall("^If", zen, re.MULTILINE)
print(m)

import glob
import re
import os


file = glob.glob("test2/*.text")
print(file)


for f in glob.glob("test2/*.text"):
	print(os.path.split(f)[1])


file = print(glob.glob('test2/**/*.txt', recursive=True))
print(file)


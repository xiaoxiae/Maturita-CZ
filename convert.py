import subprocess
from glob import glob
import os

# go through markdown files in the current directory
for file_name in glob("*.md"):
    # skip README.md
    if file_name == "README.md":
        continue

    # create the pandoc command
    command = 'pandoc "%s" -o "%s" -V %s' % (file_name,
                                             "Export/%s.pdf" % file_name[:-3],
                                             "geometry:margin=1.5cm")

    # execute the command
    os.system(command)

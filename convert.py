import subprocess
import glob
import os

# go through markdown files in the current directory
for fileName in glob.glob("*.md"):
    # parameters for the pandoc terminal command
    inputFileName = '"'+fileName+'"'
    inputFilePath = '"'+fileName.split(".")[0]+'.pdf"'
    texParameters = "-V geometry:margin=1.5cm"

    # create the pandoc command
    command = "pandoc "+inputFileName+" -o "+inputFilePath+" "+texParameters

    # execute the command
    os.system(command)

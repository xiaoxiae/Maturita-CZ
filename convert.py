#!/usr/bin/env python3

import os
import shutil
from glob import glob
from subprocess import PIPE, Popen

SOURCE_DIR = "díla"
OUTPUT_DIR = "pdf_output"

# check that pandoc is installed
if shutil.which("pandoc") is None:
    raise Exception(f"Pandoc není nainstalovaný/spustitelný!")

# move working directory to this file's
os.chdir(os.path.abspath(os.path.dirname(__file__)))

# ensure the output dir exists
if not os.path.isdir(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)

# go through markdown files in the current directory
for file_path in sorted(glob(os.path.join(SOURCE_DIR, "*.md"))):
    print(f"Převádím '{file_path}'")

    file_name = os.path.basename(file_path)
    file_name_noext = os.path.splitext(file_name)[0]

    # skip README.md
    if file_name.lower() == "README.md".lower():
        continue

    # execute the command
    process = Popen(
        [
            "pandoc",
            file_path,
            "-o",
            f"{os.path.join(OUTPUT_DIR, file_name_noext + '.pdf')}",
            "-V",
            "geometry:margin=1.5cm",
        ],
        stdout=PIPE,
        stderr=PIPE,
    )

    stdout, stderr = process.communicate()

    if process.returncode != 0:
        raise Exception(f"Při běhu Pandocu nastala chyba: {stderr.decode()}")

from os.path import getmtime
from pathlib import Path
from subprocess import run
from datetime import datetime
import re

FILE_PATH = Path.cwd()/"README.md"
TITLE = "# the-bit\n"
TODAY = datetime.today().date()
MESSAGE = f"On {TODAY}, I committed to the bit!"

def update_log(contents):
    if not contents:
        return
    with open(FILE_PATH, "w") as f:
        f.write(contents)
    try:
        run(["git", "add", FILE_PATH])
        run(["git", "commit", "-m", "Committing to the bit!"])
        run(["git", "push"]) 
    except Exception as e:
        print(f"An error occurred: {e}")

def date_modified(file):
    time_modified = getmtime(file)
    return datetime.fromtimestamp(time_modified).date()

def main():
    if FILE_PATH.is_file():
        if date_modified(FILE_PATH) < TODAY:
            with open(FILE_PATH, "r") as f:
                file_contents = f.read()
            reg = re.compile(r"(?P<title>#.*?\n)(?P<log>.*)", re.S)
            parsed_file = reg.match(file_contents)
            contents = TITLE + MESSAGE + "\n\n" + parsed_file.group("log")
        else:
            contents = ""
    else:
        contents = TITLE + MESSAGE
    update_log(contents)


if  __name__ == "__main__":
    main()
from pathlib import Path
from subprocess import run
from datetime import datetime
import re
from dateutil import parser

FILE_PATH = Path.cwd()/"README.md"
TITLE = "# the-bit\n"
TODAY = datetime.today().date()
MESSAGE = f"On {TODAY}, I committed to the bit!\n"
REG = re.compile(r"(?P<title>#.*?\n\n)(?P<latest>.*?\n)(?P<log>.*)", re.S)

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

def main():
    if FILE_PATH.is_file():
        with open(FILE_PATH) as f:
            file_contents = f.read()
        parsed_file = REG.match(file_contents)
        if parsed_file:
            latest = parsed_file.group("latest")
            log = parsed_file.group("log")
            latest_date = parser.parse(latest, fuzzy=True).date()
            if latest_date<TODAY:
                contents = TITLE + "\n" + MESSAGE + "\n" + latest + log
            else:
                contents = ""
        else:
            contents = TITLE + MESSAGE
    update_log(contents)

if  __name__ == "__main__":
    main()

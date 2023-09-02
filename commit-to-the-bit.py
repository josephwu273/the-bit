from os.path import getmtime
from pathlib import Path
from subprocess import run
from datetime import datetime

FILE_PATH = Path.cwd()/"bit.log"
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


if  __name__ == "__main__":
    if FILE_PATH.is_file():
        if date_modified(FILE_PATH) < TODAY:
            with open(FILE_PATH, "r") as f:
                file_contents = f.read()
            contents = MESSAGE + "\n" + file_contents
        else:
            contents = ""
    else:
        contents = MESSAGE
    update_log(contents)
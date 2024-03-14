import os
import subprocess as sp

while True:
    terminal = input(">> ")
    if terminal == "ls":
        sp.run(["dir", "/a"], shell=True)
    elif terminal == "calc":
        sp.run(["calc"], shell=True)
    elif terminal.startswith("listprocs "):
        process_name = terminal.split(maxsplit=1)[1]
        sp.run(["tasklist", "|", "findstr", process_name], shell=True)
    elif terminal.startswith("chdir "):
        directory = terminal.split(maxsplit=1)[1]
        try:
            os.chdir(directory)
            print(f"Directory changed to {directory}")
        except FileNotFoundError:
            print(f"Directory not found: {directory}")
    else:
        print("Command not recognized.")

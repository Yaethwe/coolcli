import json, os, sys, sqlite3

HELP = """

Cool Command Line Tool (CCLT)
Version >>> 1.0

Python Version
    3.11+

Command Line Arguments

 "--help" or "-h" to get help menu.

 "run" or "." to run something.
    "mode" to run a mode
        "python" -> python code executor mode.
        "cli" -> to run your conventional cli commands either your are using batch or command prompt
	
CLI commands
 "commands" -> to show all commands.
 
"""
allcommands=[
{"name": ["cd"],"info":"to change dir."},
{"name": ["cls","clear"],"info":"to clear console."},
{"name": ["l","ls","list","listdir","dir"],"info":"to list files and dirs in current dir."},
{"name": ["mkdir", "md"],"info":"to create dir."},
{"name": ["exit","quit"],"info":"to exit the  app."},
]

def create_file(name = "newfile", extension=".txt", data = " ", *args, **kwargs):
    file_name = ""
    if extension=="none":
        file_name = name
    else:   
        file_name = name + extension
        
    with open(file_name, 'w') as file:
        file.write(data)

def match(data, *args):
    if data:
        for i in args:
            if data == i:
                return True
                break
            
    return False        

def print_listed_dir():
    for i in os.listdir():
        if os.path.isfile(i):
            print(f"<file>,  name: {i}, size: {os.stat(i).st_size}byte(s)")
        elif os.path.isdir(i):
            print(f"<dir>,  name: {i}, size: {os.stat(i).st_size}byte(s)")

def cli(modein = "cli"):
    running = True
    command = ""
    cursor = ">"
    show_pwd = False
    mode = modein
    pwd = os.getcwd()
    concur = cursor
    skip_loop = False
    def update_pwd():
        global pwd, concur
        if show_pwd:
            concur = os.getcwd()+cursor

    while running:
        command = input(f"{concur} ")

        if command == "exit" or command == "quit":
            running = False
            
        elif command == "createfile" or command == "cf":
            file_name = input("File Name: ") or "newfile"
            file_extension = input("File Extension: ") or ".txt"
            file_data = input("File Data: ") or " "
            create_file(file_name, file_extension, file_data)
            
        elif match(command, "list", "ls", "l", "dir", "listdir"):
            print_listed_dir()
            update_pwd()
            
        elif match(command, "clear", "cls"):
            try:
                os.system("clear")
            except:
                os.system("cls")
            update_pwd()
            
        elif match(command, "mkdir", "md", "makedir"):
            os.mkdir(input("Dir Name: ") or "newdir")
            
        elif match(command, "pwd", "whereami"):
            print(os.getcwd())
            
        elif match(command, "setcursor", "sc"):
            cursor = input("Enter Custom Cursor: ") or ">"
            
        elif match(command, "setmode", "sm"):
            mode = input("Enter Mode Name: ") or "python"
        
        elif command == "cd":
            dirc = input("Enter Dir Name: ") or "./"
            os.chdir(dirc)
            update_pwd()
        
        elif command == "enablepwd":
            show_pwd = True
            update_pwd()
        
        elif command == ".passloop":
            skip_loop = True
            running = False
            
        elif command == "commands":
            line = ""
            for i in allcommands:
                for j in i["name"]:
                    line = line + "\"" + j + "\", "
                line = line + " -> " + i["info"] + '\n'
            print(line)
        else:
            if mode == "python":
                try:
                    exec(command)
                except OSError as err:
                    print("OS error:", err)
                except ValueError:
                    print("Could not convert data to an integer.")
                except Exception as err:
                    print(f"Unexpected {err=}, {type(err)=}")
            
            elif mode == "cli":
                try:
                    os.system(command)
                except:
                    print("Command execution error.")
       
            else:
                print(f"There is no command named \"{command}\".")
                
    if not skip_loop:
        quit()

if match(sys.argv[0], "--help", "-h"):
    print(HELP)
elif match(sys.argv[1], "run", "."):
    if sys.argv[2] == "mode" and sys.argv[3]:
        cli(sys.argv[3])
else:
    print(HELP)

import sys
import shutil 
import subprocess
import os

def exit(command_parts):
    if len(command_parts) > 1:
        sys.exit(int(command_parts[1]))
    sys.exit(0)

def echo(command_parts): 
    print(" ".join(command_parts[1:]).replace("'", ""))

def type(command_parts):

    BUILTINS = ["exit", "echo", "type", "pwd"]
    
    if len(command_parts) > 1:    
        if(command_parts[1] in BUILTINS):
            print(f"{command_parts[1]} is a shell builtin")
        else:
            if found_command_in_path := shutil.which(command_parts[1]):
                    print(f"{command_parts[1]} is {found_command_in_path}")
            else:
                print(f"{command_parts[1]}: not found")

def pwd(command_parts):
    print(os.getcwd())

def cd(command_parts):
    if len(command_parts) < 2:
        print("cd: missing operand")
        return
    
    complete_path = command_parts[1]

    if complete_path.startswith("~"):
        complete_path = os.path.expanduser(complete_path)

    new_path = os.path.normpath(os.path.abspath(os.path.join(os.getcwd(), complete_path)))

    if os.path.exists(new_path) and os.path.isdir(new_path):
        os.chdir(new_path)
    else:
        print(f"cd: {complete_path}: No such file or directory") 

import os

def cat(command_parts):
    if len(command_parts) < 2:
        print("cat: missing operand")
        return

    filename = " ".join(command_parts[1:])   

    if not os.path.exists(filename):
        print(f"cat: {filename}: No such file or directory")
        return

    if not os.path.isfile(filename):
        print(f"cat: {filename}: Is a directory")
        return

    try:
        with open(filename, "r", encoding="utf-8") as file:
            print(file.read(), end="")  
    except Exception as e:
        print(f"cat: {filename}: {e}")

def main():
    
    while(True):
        sys.stdout.write("$ ")

        command = input()

        command_parts = command.split(" ")

        match command_parts[0]:
            case "exit":
                exit(command_parts)
            case "echo":
                echo(command_parts)
            case "type":
                type(command_parts)
            case "pwd":
                pwd(command_parts)
            case "cd":
                cd(command_parts)
            case _:
                # If the command exist in PATH
                if shutil.which(command_parts[0]):
                    subprocess.run(command_parts)
                else:
                    print(f"{command}: command not found")

if __name__ == "__main__":
    main()
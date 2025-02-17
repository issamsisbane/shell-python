import sys
import os

def exit(command_parts):
    if len(command_parts) > 1:
        sys.exit(int(command_parts[1]))
    sys.exit(0)

def echo(command_parts):
    print(" ".join(command_parts[1:]))

def type(command_parts):

    BUILTINS = ["exit", "echo", "type"]
    
    if len(command_parts) > 1:    
        if(command_parts[1] in BUILTINS):
            print(f"{command_parts[1]} is a shell builtin")
        else:
            found_command_in_path = search_command_in_path(command_parts[1])
            if found_command_in_path is not None:
                    print(f"{command_parts[1]} is {found_command_in_path}")
            else:
                print(f"{command_parts[1]}: not found")

def search_command_in_path(command_to_find):
    PATH = os.getenv("PATH")

    folders_to_search = PATH.split(":")
    for folder_to_search in folders_to_search:
        if command_to_find in os.listdir(folder_to_search):
            return f"{folder_to_search}/{command_to_find}"
    return None

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
            case _:
                print(f"{command}: command not found")

if __name__ == "__main__":
    main()
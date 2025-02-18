import sys
import shutil 

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
            if found_command_in_path := shutil.which(command_parts[1]):
                    print(f"{command_parts[1]} is {found_command_in_path}")
            else:
                print(f"{command_parts[1]}: not found")

def search_command_in_path(command_to_find):
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
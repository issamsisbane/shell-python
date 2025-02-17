import sys


def main():

    while(True):
        sys.stdout.write("$ ")

        command = input()

        command_parts = command.split(" ")

        if (command_parts[0] == "exit"):
            if len(command_parts) > 1:
                sys.exit(command_parts[1])

        print(f"{command}: command not found")

if __name__ == "__main__":
    main()

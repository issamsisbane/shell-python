import sys


def main():

    while(True):
        sys.stdout.write("$ ")

        command = input()

        command_parts = command.split(" ")

        match command_parts[0]:
            case "exit":
                if len(command_parts) > 1:
                    sys.exit(int(command_parts[1]))
                sys.exit(0)
            case "echo":
                print(" ".join(command_parts[1:]))
            case _:
                print(f"{command}: command not found")

if __name__ == "__main__":
    main()

import functions
import os, sys

def main():
    os.system('cls')
    functions.project_name()
    action = functions.get_action()
    if (action == 1):
        message = functions.get_message()
        fileName = functions.get_image()
        if functions.confirmation() == False:
            print("Exiting program\n")
            return None
        functions.hide_the_message(message, fileName)
        sys.exit()
    elif (action == 2):
        fileName = functions.get_hidden_image()
        functions.find_the_message(fileName)
        sys.exit()
    else:
        sys.exit()


if __name__ == '__main__':
    main()
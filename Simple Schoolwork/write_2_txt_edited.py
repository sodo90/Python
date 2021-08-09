import os


def main():

    # Asks user for path chose and then checks whether the path exists
    # If path does not exist main() is called again to restart the program
    directory = input("Type the directory path: ")
    if os.path.isdir(directory):
        pass
    else:
        input('That path does not exist press "ENTER" to retry')
        main()

    # Asks user to choose a filename to save file as
    # Then checks to see if the file name contains filetype suffix
    # If name does not contain suffix .txt is appended if suffix is not of type .txt the suffix is changed
    filename = input("Save as filename: ")
    if '.txt'.lower() not in filename:
        if len(filename) < 4:
            filename = filename + '.txt'
        else:
            changename = filename.split('.')
            filename = changename[0] + '.txt'

    # List is used to ask user for Name, Address, and Phone number
    info = [input('Name: '), input('Address: '), input('Phone Number: ')]

    # Opens chosen file path and creates or opens chosen filename
    # List containing user info is then written to the file joined together with ', '
    with open(directory + '\\' + filename, 'a+') as file:
        file.write(', '.join(info))
        file.write('\n')

    # Chosen path and file are opened again to print the newly appended data.
    with open(directory + '\\' + filename, 'r') as file:
        data = file.readlines()
        prettylength = 0
        for line in data:
            if prettylength < len(directory + '\\' + filename):
                prettylength = len(directory + '\\' + filename)
            elif prettylength < len(line):
                prettylength = len(line)
        print('\n')
        print('*' * int(prettylength))
        print('Filename: ', file.name)
        print('-' * int(prettylength))
        for line in data:
            print(line.replace('\n', ''))
        print('*' * int(prettylength))
        input('Press ENTER to end the program')


# Main entry into program
if __name__ == '__main__':
    main()

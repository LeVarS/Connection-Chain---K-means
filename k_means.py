""" Executes the K means algorithm on a file containing SEND, ECHO, and ACK TCP packets

Using the simplified text file of the tcpdump capture file, this script will
organize those packets into clusters using the K means clustering algorithm.

This program can read from a list containing multiple file names or can take the
name of one file if testing isn't needed for multiple files.


"""

def valid_filename(file_name):
    file = None
    if file_name == "":
        file_name = input("Enter the name of the file: ")
    if ".txt" not in file_name:
        file_name += ".txt"
    try:
        file = open(file_name, "r")
    except FileNotFoundError as e:
        print("Unable to open %s." % file_name)
        print("File may not be in current directory or may not exist.")
        #return file
    return file

def main():
    print("K Means Clustering Program.")
    print("This script is able to read and execute the algorithm on one text file or a text file containing the names of other text files.")
    choice = input("Enter 1 to execute one text file or 2 to execute the file that contains other file names or anything else to exit: ")

    file = None

    if choice == "1":
        file = valid_filename("")
        if (file == None):
            exit(-1)
        print("Succesful open")

    elif choice == "2":
        file = valid_filename("")
        if (file == None):
            exit(-1)

        file_list = []
        invalid = " \n@!#$%^&*()+=?><,{}[]|\\~\`\'\"/"
        # Reads through every line and retrieves the file name
        for line in file:
            file_name = ""
            for char in line:
                if char not in invalid:
                    file_name += char
                    if len(file_name) > 4:
                        if file_name[len(file_name) -4:] == ".txt":
                            file_list.append(file_name)
                            file_name = ""
            if file_name != "":
                file_list.append(file_name)

        # Close initial file
        file.close()

        for file_name in file_list:
            #file = None
            file = valid_filename(file_name)
            if (file == None):
                print("Unable to continue. Moving on from", file_name)


    if (not file == None):
        file.close()

    exit(0)


if __name__ == "__main__":
    main()

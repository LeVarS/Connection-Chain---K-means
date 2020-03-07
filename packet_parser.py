""" Reads a txt file that is made by running tcpdump

Reads through the text file and writes the timestamp as wll as the type of the
packet (Send, Echo, or Ack) to a new file for later testing with the
K-means algorithm.

Change the value of 'file_name' to match the file that needs to be parsed
through.

Can also change the name of the 'write_file' if another file name is needed.

"""

def main():
    file_name = "myCapture2.txt"

    try:
        read_file = open(file_name, "r")
    except FileNotFoundError as e:
        print("Unable to open %s." % file_name)
        print("File may not be in current directory or may not exist.")
        exit(-1)

    write_file = open("parsed.txt", "w")

    for line in read_file:

        arr = line.split(" ")

        if ":" in arr[0]:
            timestamp = arr[0]
            # src_ip = arr[2]
            src_port = arr[2].split(".")[4].split(":")[0]
            # dst_ip = arr[4]
            dst_port = arr[4].split(".")[4].split(":")[0]
            type = arr[6]

            if "P" in type:
                if src_port == "22" or src_port == "ssh":
                    type = "ECHO"
                else:
                    type = "SEND"
            else:
                type = "ACK"

            write_file.write(timestamp + "\t\t" + type + "\n")

    read_file.close()
    write_file.close()


if __name__ == "__main__":
    main()

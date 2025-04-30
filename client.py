import socket

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 8080

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
    except ConnectionRefusedError:
        print("Connection failed. Make sure the server is running.")
        exit()

    filename = input("Enter the name of the file to transfer: ")
    try:
        with open(filename, 'r') as fi:
            data = fi.read(1024)
            while data:
                sock.send(data.encode())
                data = fi.read(1024)
    except IOError:
        print("Invalid filename. Please try again.")

    sock.close()

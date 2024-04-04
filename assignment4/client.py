import socket

def main():
    # Create a socket object
    s = socket.socket()
    print("Socket created")

    # Define the port on which you want to connect
    port = 8080

    s.connect(('127.0.0.1', port))

if __name__ == "__main__":
    main()
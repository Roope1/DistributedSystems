import socket

def main():
    # Create a socket object
    s = socket.socket()
    print("Socket created")

    # Define the port on which you want to connect
    port = 8080

    s.bind(('', port))

    # put the socket into listening mode
    s.listen(5)

    print("socket is listening")

    # a forever loop until we interrupt it or an error occurs
    while True:
        # Establish connection with client.
        c, addr = s.accept()
        print('Got connection from', addr)

        # send a thank you message to the client.
        c.send('Thank you for connecting'.encode())

        # Close the connection with the client
        c.close()

if __name__ == "__main__":
    main()
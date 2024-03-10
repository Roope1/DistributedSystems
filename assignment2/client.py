from xmlrpc.client import ServerProxy
from datetime import datetime

PROXY_ADDRESS = "http://127.0.0.1:8000/RPC2"


class Message:
    """Class is used to represent the message that will be sent to the server"""

    def __init__(self, topic: str, note: str, text: str) -> None:
        self.topic: str = topic
        self.note: str = note
        self.text: str = text
        self.timestamp: datetime = datetime.now().isoformat()


def get_user_input() -> Message:
    """Used to get the user input and create a Message object based on it"""
    topic = input("Enter the topic of the message: ")
    note = input("Enter a note for the message: ")
    content = input("Enter the content of the message: ")
    return Message(topic, note, content)


def send_message(msg: Message) -> str:
    """Used for sending a message to the server"""
    try:
        with ServerProxy(PROXY_ADDRESS) as proxy:
            # Objects can be sent but only their __dict__ attribute is used, which is fine
            proxy.add_new(msg)

    except ConnectionRefusedError:
        print("Could not connect to server.")


def get_topic(topic: str) -> str:
    """Get a topic from server"""
    try:
        with ServerProxy(PROXY_ADDRESS) as proxy:
            return proxy.get_topic(topic)

    except ConnectionRefusedError:
        print("Could not connect to server.")


def main():
    while True:
        print("What do you want to do?")
        print("1. Add a new note")
        print("2. Get an existing topic")
        print("3. Exit")
        try:
            choice = int(input())
            match choice:
                case 1:
                    msg = get_user_input()
                    send_message(msg)
                case 2:
                    topic = input("Enter the topic: ")
                    print(get_topic(topic))
                case 3:
                    break
                case _:
                    print("Invalid input")
                    continue
        except ValueError:
            print("Invalid input")
            continue

if __name__ == "__main__":
    main()

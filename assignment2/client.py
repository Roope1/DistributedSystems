from xmlrpc.client import ServerProxy
from datetime import datetime

PROXY_ADDRESS = "http://127.0.0.1:8000/RPC2"


class Message:
    """Class is used to represent the message that will be sent to the server"""

    def __init__(self, topic: str, content: str) -> None:
        self.topic: str = topic
        self.content: str = content
        self.timestamp: datetime = datetime.now().isoformat()


def get_user_input() -> Message:
    """Used to get the user input and create a Message object based on it"""
    topic = input("Enter the topic of the message: ")
    content = input("Enter the content of the message: ")
    return Message(topic, content)


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
    # get the user input and create a Message object based on it
    #msg = get_user_input()
    #send_message(msg)
    topic = input("Enter the topic: ")
    print(get_topic(topic))

if __name__ == "__main__":
    main()

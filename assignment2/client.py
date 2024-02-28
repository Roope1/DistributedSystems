from xmlrpc.client import ServerProxy

def main():
    with ServerProxy("http://127.0.0.1:8000/RPC2") as proxy:
        print(proxy.add_new("This is a test message"))

if __name__ == "__main__":
    main()
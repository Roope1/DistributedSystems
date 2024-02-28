from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
import xml.etree.ElementTree as ET

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ("/RPC2",)


def main():
    with (SimpleXMLRPCServer(("127.0.0.1", 8000), requestHandler=RequestHandler)) as server:
        server.register_introspection_functions()

        @server.register_function(name="add_new")
        def add_new(content):
            print(content)
            return "OK"

        @server.register_function(name="get_topic")
        def get_topic(topic):
            # Open the "database" xml file
            with (open("db.xml", "r")) as f:
                # Parse the xml file
                root = ET.fromstring(f.read())
                # find by topic
                res = root.findall(f"./topic[@name='{topic}']")
                if (len(res) > 0):
                    return ET.tostring(res[0], encoding="unicode")
                else: 
                    return "No topic found."

        server.serve_forever()


if __name__ == "__main__":
    main()

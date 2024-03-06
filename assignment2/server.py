from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
import xml.etree.ElementTree as ET

PORT = 8000

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ("/RPC2",)


def main():
    with (SimpleXMLRPCServer(("127.0.0.1", PORT), requestHandler=RequestHandler)) as server:
        server.register_introspection_functions()

        @server.register_function(name="add_new")
        def add_new(content):
            print(content)
            # Open the "database" xml file
            with (open("db.xml", "r")) as f:
                # read the existing "db"
                root = ET.fromstring(f.read())
            # try find the topic
            print("got here")
            res = root.findall(f"./topic[@name='{content['topic']}']")
            # if topic exists append to it 
            if (len(res) > 0):
                # TODO: append new item
                pass 
            # else create a new topic
            else: 
                new_topic = ET.Element("topic")
                new_topic.attrib["name"] = content["topic"]
                new_content = ET.SubElement(new_topic, "content")
                new_content.text = content["content"]
                root.append(new_topic)
                print("new topic created")
                # write to file
                with (open("db.xml", "w")) as f:
                    f.write(ET.tostring(root, encoding="unicode"))
                    print("file written")
                    
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

        print(f"listening on port {PORT}")
        server.serve_forever()

if __name__ == "__main__":
    main()

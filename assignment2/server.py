from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
import xml.etree.ElementTree as ET

PORT = 8000

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ("/RPC2",)


def create_new_note(topic, content):
    new_note = ET.SubElement(topic, "note")
    new_note.attrib["name"] = content["note"]
    new_content = ET.SubElement(new_note, "text")
    new_content.text = content["text"]
    new_timestamp = ET.SubElement(new_note, "timestamp")
    new_timestamp.text = content["timestamp"]
    return new_note

def create_new_topic(content):
    new_topic = ET.Element("topic")
    new_topic.attrib["name"] = content["topic"]
    new_note = create_new_note(new_topic, content)

    return new_topic

def main():
    with (SimpleXMLRPCServer(("127.0.0.1", PORT), requestHandler=RequestHandler)) as server:
        server.register_introspection_functions()

        @server.register_function(name="add_new")
        def add_new(content):
            # Open the "database" xml file
            with (open("db.xml", "r")) as f:
                # read the existing "db"
                root = ET.fromstring(f.read())
            # try find the topic
            res = root.findall(f"./topic[@name='{content['topic']}']")
            # if topic exists append to it 
            if (len(res) > 0):
                create_new_note(res[0], content)
                with (open("db.xml", "w")) as f:
                    f.write(ET.tostring(root, encoding="unicode"))
                    print("file written")
                return "OK"
            # else create a new topic
            else: 
                root.append(create_new_topic(content))
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

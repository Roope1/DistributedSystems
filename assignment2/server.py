from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ("/RPC2",)

def main():
    with (SimpleXMLRPCServer(("127.0.0.1", 8000), requestHandler=RequestHandler)) as server:
        server.register_introspection_functions()

        @server.register_function(name="add_new")
        def add_new(content: str):
            print(content)
            return "OK"

       
        server.serve_forever()
    


if __name__ == "__main__":
    main()
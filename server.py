import argparse
from flask import Flask
from key_value_store import KeyValueStore

class Server:
    app = Flask(__name__)

    def __init__(self, hostname="127.0.0.1", port=50050):
        self.hostname = hostname
        self.port = port
        self.kv_store = KeyValueStore()

    def ping(self):
        return {"status": "OK!"}


    def get(self, key):
        result = self.kv_store.get(key)
        print("Result: {}".format(result))
        return {"result": result}

    def run(self):
        self.app.run(self.hostname, self.port)


app = Server.app
@app.route('/api/<key>', methods=['GET'])
def get(key):
    return server.get(key)

@app.route('/api/ping')
def ping():
    return server.ping()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-H", "--host", default="127.0.0.1", type=str,
                        help="hostname/IP to connect to. Default: 127.0.0.1")
    parser.add_argument("-p", "--port", default=50050, type=int,
                        help='port to connect to. Default: 50050')

    args = parser.parse_args()
    global server
    server = Server(args.host, args.port)
    server.run()

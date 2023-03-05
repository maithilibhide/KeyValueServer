import argparse
import requests

class Client:
    def __init__(self, hostname="127.0.0.1", port=50050):
        self.hostname = hostname
        self.port = port
        self.url = f"http://{hostname}:{port}/api"
        self._check_client_connection()

    def _check_client_connection(self):
        try:
            requests.get(f"{self.url}/ping")
        except requests.exceptions.ConnectionError:
            print(f"Couldn't connect to {self.host}:{self.port}!",
                  "Make sure the KeyValueStore REST server is running.")
            self.exit(1)
        except Exception as e:
            print(f"Unexpected error! {err}", e)
            self.exit(1)

    def execute(self, cmd, *args):
        if cmd.upper() == "GET":
            if len(args) != 1:
                raise ValueError("Expected one key found {}!".format(len(args)))
            key = args[0]
            response = requests.get(f"{self.url}/{key}")
            print(response)
            return response.json()["result"]
        else:
            raise NotImplementedError("Currently we can only retrieve keys from the KV Store!")

    def io_loop(self):
        while True:
            input_data = input("Enter key: ")
            if not input_data:
                break

            cmd, *args = "GET", input_data.strip()
            response = self.execute(cmd, *args)
            print(response)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-H", "--host", default="127.0.0.1", type=str,
                        help="hostname/IP to connect to. Default: 127.0.0.1")
    parser.add_argument("-p", "--port", default=50050, type=int,
                        help='port to connect to. Default: 50050')

    args = parser.parse_args()
    client = Client(args.host, args.port)
    client.io_loop()
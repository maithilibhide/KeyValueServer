import requests

class KeyValueStore:
    URL = "https://raw.githubusercontent.com/savingoyal/systems-assignment/main/example.data"
    NEWLINE_SEP = "\n"
    SPACE_SEP = " "

    def __init__(self, url=URL):
        self.url = url
        self.hashmap = {}
        self._initialize_kv_store()

    def _read_url_data(self):
        response = requests.get(self.url)
        data = response.text
        return data

    def _initialize_kv_store(self):
        data = self._read_url_data()
        for i, line in enumerate(data.split(KeyValueStore.NEWLINE_SEP)):
            line = line.split(KeyValueStore.SPACE_SEP)
            key, val = line[0], line[1:]
            self.hashmap[key] = KeyValueStore.SPACE_SEP.join(val)

    def get(self, key):
        print("Lookup: {}".format(key))
        if key in self.hashmap:
            return self.hashmap[key]
        return None

    def set(self, key, value):
        self.hashmap[key] = value

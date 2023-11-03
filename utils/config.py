import os
import json

class config:
    def read() -> dict:
        return json.load(open(str(os.path.expanduser('config.json'))))
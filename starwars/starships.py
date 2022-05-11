import starwars.app.requesting_sw as rq
import json


class Starships:

    # Class attributes
    def __init__(self):
        self.content = {}
        self.starships = {}

    # Requesting data from api using request import
    # Converts bjson to json, stores as dictionary
    def requesting(self):
        try:
            self.content = json.loads(rq.sw.content)
            print("Code 200: request successful")
        except:
            raise
        finally:
            print("Requests Executed")

        return self.content

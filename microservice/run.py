import time

from cache import Cache
from client import Client
from server import Server

if __name__ == "__main__":
    cache = Cache("data.json")
    client = Client(cache)
    server = Server(client, 10)

    while True:
        client.fetch_data()
        time.sleep(1)

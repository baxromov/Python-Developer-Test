import json
import time

from utlis import fetch_data

ENDPOINT_URLS = ["http://app:8001/data"]
PERIODS = [15, 30, 60]


class Client:
    def __init__(self, cache):
        self.cache = cache
        self.last_fetch_time = [0] * len(ENDPOINT_URLS)

    def fetch_data(self):
        for i in range(len(ENDPOINT_URLS)):
            if time.time() - self.last_fetch_time[i] >= PERIODS[i]:
                host, port = self.get_host_port(ENDPOINT_URLS[i])
                data = fetch_data(host, port)
                self.cache.add_data(data)
                self.last_fetch_time[i] = time.time()

    def get_data(self):
        return json.dumps(self.cache.get_data())

    def get_host_port(self, url):
        host = url.split("//")[1].split(":")[0]
        port = url.split("//")[1].split(":")[1]
        return host, port

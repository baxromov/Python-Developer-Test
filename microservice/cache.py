import json
import time

CACHE_EXPIRATION = 120


class Cache:
    def __init__(self, file_path):
        self.cache = {}
        self.file_path = file_path
        self.load_cache()

    def add_data(self, data):
        for item in data:
            self.cache[item] = time.time()
        self.save_cache()

    def get_data(self):
        now = time.time()
        data = list(self.cache.keys())
        for item in data:
            if now - self.cache[item] > CACHE_EXPIRATION:
                del self.cache[item]
        self.save_cache()
        return list(self.cache.keys())

    def save_cache(self):
        with open(self.file_path, "w") as f:
            json.dump(self.cache, f)

    def load_cache(self):
        try:
            with open(self.file_path, "r") as f:
                self.cache = json.load(f)
        except:
            pass

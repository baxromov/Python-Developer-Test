import json
import time
import unittest

from cache import Cache, CACHE_EXPIRATION


class TestCache(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_cache.json"
        self.cache = Cache(self.file_path)

    def tearDown(self):
        self.cache.cache = {}
        with open(self.file_path, "w") as f:
            f.write("[]")

    def test_add_data(self):
        data = ["a", "b", "c"]
        self.cache.add_data(data)
        with open(self.file_path, "r") as f:
            cached_data = json.load(f)
        self.assertEqual(set(data), set(cached_data.keys()))

    def test_get_data(self):
        data = ["a", "b", "c"]
        self.cache.cache = {d: time.time() for d in data}
        with open(self.file_path, "w") as f:
            json.dump(self.cache.cache, f)
        self.assertEqual(self.cache.get_data(), data)

    def test_expired_data(self):
        data = ["a", "b", "c"]
        self.cache.cache = {d: time.time() - CACHE_EXPIRATION - 1 for d in data}
        with open(self.file_path, "w") as f:
            json.dump(self.cache.cache, f)
        self.assertEqual(self.cache.get_data(), [])

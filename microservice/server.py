class Server:
    def __init__(self, client, max_clients):
        self.client = client
        self.max_clients = max_clients
        self.num_clients = 0

    def handle_request(self):
        if self.num_clients < self.max_clients:
            self.num_clients += 1
            return self.client.get_data(), 200
        else:
            return "Too many clients", 429

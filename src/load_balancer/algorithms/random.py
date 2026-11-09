import random

from ..server_pool import ServerPool


class Random:
    def __init__(self, server_pool: ServerPool):
        self.server_pool = server_pool

    def get_next_server(self):
        servers = self.server_pool.get_healthy_servers()

        if not servers:
            return None

        return random.choice(servers)
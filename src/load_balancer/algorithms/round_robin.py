from ..server_pool import ServerPool


class RoundRobin:
    def __init__(self, server_pool: ServerPool):
        self.server_pool = server_pool
        self.current_index = 0

    def get_next_server(self):
        servers = self.server_pool.get_healthy_servers()

        if not servers:
            return None

        server = servers[self.current_index % len(servers)]
        self.current_index += 1

        return server
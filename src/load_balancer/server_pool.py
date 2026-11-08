from .server import Server


class ServerPool:
    def __init__(self):
        self.servers: list[Server] = []

    def add_server(self, server: Server) -> None:
        self.servers.append(server)

    def get_healthy_servers(self) -> list[Server]:
        return [
            server for server in self.servers
            if server.is_healthy
        ]
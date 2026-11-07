from dataclasses import dataclass


@dataclass
class Server:
    host: str
    port: int
    active_connections: int = 0
    is_healthy: bool = True

    @property
    def url(self) -> str:
        return f"http://{self.host}:{self.port}"
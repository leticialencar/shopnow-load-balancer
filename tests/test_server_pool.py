from load_balancer.server import Server
from load_balancer.server_pool import ServerPool


def test_server_pool_adds_servers():
    pool = ServerPool()

    server = Server("127.0.0.1", 5001)
    pool.add_server(server)

    assert len(pool.servers) == 1
    assert pool.servers[0] == server


def test_server_pool_returns_only_healthy_servers():
    pool = ServerPool()

    healthy_server = Server("127.0.0.1", 5001)
    unhealthy_server = Server("127.0.0.1", 5002, is_healthy=False)

    pool.add_server(healthy_server)
    pool.add_server(unhealthy_server)

    healthy_servers = pool.get_healthy_servers()

    assert healthy_servers == [healthy_server]


def test_server_pool_returns_empty_list_when_no_servers_are_healthy():
    pool = ServerPool()

    pool.add_server(Server("127.0.0.1", 5001, is_healthy=False))

    assert pool.get_healthy_servers() == []
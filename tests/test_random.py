
from load_balancer.server import Server
from load_balancer.server_pool import ServerPool
from load_balancer.algorithms.random import Random


def test_random_selects_a_server_from_available_servers():
    pool = ServerPool()

    servers = [
        Server("127.0.0.1", 5001),
        Server("127.0.0.1", 5002),
        Server("127.0.0.1", 5003),
    ]

    for server in servers:
        pool.add_server(server)

    balancer = Random(pool)

    selected_server = balancer.get_next_server()

    assert selected_server in servers


def test_random_ignores_unhealthy_servers():
    pool = ServerPool()

    healthy_server = Server("127.0.0.1", 5001)
    unhealthy_server = Server("127.0.0.1", 5002, is_healthy=False)

    pool.add_server(healthy_server)
    pool.add_server(unhealthy_server)

    balancer = Random(pool)

    for _ in range(10):
        assert balancer.get_next_server() == healthy_server


def test_random_returns_none_when_no_servers_are_healthy():
    pool = ServerPool()

    pool.add_server(
        Server("127.0.0.1", 5001, is_healthy=False)
    )

    balancer = Random(pool)

    assert balancer.get_next_server() is None

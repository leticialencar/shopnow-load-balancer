
from load_balancer.server import Server
from load_balancer.server_pool import ServerPool
from load_balancer.algorithms.least_connections import LeastConnections


def test_least_connections_selects_server_with_fewest_connections():
    pool = ServerPool()

    server1 = Server("127.0.0.1", 5001, active_connections=5)
    server2 = Server("127.0.0.1", 5002, active_connections=2)
    server3 = Server("127.0.0.1", 5003, active_connections=8)

    pool.add_server(server1)
    pool.add_server(server2)
    pool.add_server(server3)

    balancer = LeastConnections(pool)

    assert balancer.get_next_server() == server2


def test_least_connections_ignores_unhealthy_servers():
    pool = ServerPool()

    server1 = Server("127.0.0.1", 5001, active_connections=1)
    server2 = Server("127.0.0.1", 5002, active_connections=0, is_healthy=False)
    server3 = Server("127.0.0.1", 5003, active_connections=3)

    pool.add_server(server1)
    pool.add_server(server2)
    pool.add_server(server3)

    balancer = LeastConnections(pool)

    assert balancer.get_next_server() == server1


def test_least_connections_returns_none_when_no_servers_are_healthy():
    pool = ServerPool()

    pool.add_server(
        Server("127.0.0.1", 5001, is_healthy=False)
    )

    balancer = LeastConnections(pool)

    assert balancer.get_next_server() is None

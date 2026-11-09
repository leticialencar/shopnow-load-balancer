from load_balancer.server import Server
from load_balancer.server_pool import ServerPool
from load_balancer.algorithms.round_robin import RoundRobin


def test_round_robin_distributes_servers_in_order():
    pool = ServerPool()

    pool.add_server(Server("127.0.0.1", 5001))
    pool.add_server(Server("127.0.0.1", 5002))
    pool.add_server(Server("127.0.0.1", 5003))

    balancer = RoundRobin(pool)

    ports = [
        balancer.get_next_server().port
        for _ in range(6)
    ]

    assert ports == [5001, 5002, 5003, 5001, 5002, 5003]


def test_round_robin_ignores_unhealthy_servers():
    pool = ServerPool()

    pool.add_server(Server("127.0.0.1", 5001))
    pool.add_server(Server("127.0.0.1", 5002, is_healthy=False))
    pool.add_server(Server("127.0.0.1", 5003))

    balancer = RoundRobin(pool)

    ports = [
        balancer.get_next_server().port
        for _ in range(4)
    ]

    assert ports == [5001, 5003, 5001, 5003]


def test_round_robin_returns_none_when_no_servers_are_healthy():
    pool = ServerPool()

    pool.add_server(Server("127.0.0.1", 5001, is_healthy=False))

    balancer = RoundRobin(pool)

    assert balancer.get_next_server() is None
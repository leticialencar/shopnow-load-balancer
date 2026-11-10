import sys
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

PORTS = [8080, 8081, 8082]


def check_servers(endpoint):
    for port in PORTS:
        url = f"http://localhost:{port}/{endpoint}"

        print(f"\nTesting: {url}")

        try:
            with urlopen(url, timeout=3) as response:
                print(f"Status: {response.status}")
                print(f"Response: {response.read().decode()}")

        except (URLError, HTTPError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    endpoint = sys.argv[1] if len(sys.argv) > 1 else ""

    if endpoint not in ("", "health"):
        print("Invalid endpoint.")
        sys.exit(1)

    check_servers(endpoint)
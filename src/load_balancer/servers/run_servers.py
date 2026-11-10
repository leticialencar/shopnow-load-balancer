
from threading import Thread

from load_balancer.servers.app import start_server


if __name__ == "__main__":
    ports = [8080, 8081, 8082]

    for port in ports:
        Thread(
            target=start_server,
            args=(port,),
            daemon=True
        ).start()

    print("All ShopNow servers are running! :)")
    
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nShopNow servers stopped.")

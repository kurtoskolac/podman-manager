import os
import time
import platform
import subprocess
from pathlib import Path

# Docker compose YAML file path
COMPOSE_PATH = Path("/Users/username/Projects/self-hosted")


# Print banner UI function /Added check for Windows
def print_banner():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    banner = """
    ╔═════════════════════════════════════════════════════╗
    ║                                                     ║
    ║   ██████╗  ██████╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
    ║   ██╔══██╗██╔═══██╗██╔══██╗████╗ ████║██╔══██╗████╗  ██║
    ║   ██████╔╝██║   ██║██║  ██║██╔████╔██║███████║██╔██╗ ██║
    ║   ██╔═══╝ ██║   ██║██║  ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
    ║   ██║     ╚██████╔╝██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
    ║   ╚═╝      ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
    ║                                                     ║
    ║   ███╗   ███╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗███████╗
    ║   ████╗ ████║██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝
    ║   ██╔████╔██║███████║██║     ███████║██║██╔██╗ ██║█████╗  
    ║   ██║╚██╔╝██║██╔══██║██║     ██╔══██║██║██║╚██╗██║██╔══╝  
    ║   ██║ ╚═╝ ██║██║  ██║╚██████╗██║  ██║██║██║ ╚████║███████╗
    ║   ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝
    ║                                                     ║
    ║   ███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗ 
    ║   ████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗
    ║   ██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝
    ║   ██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
    ║   ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║
    ║   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
    ║                                                     ║
    ║                   v0.5 • Данијел Тарић • 14/12/2025 ║
    ║                                                     ║
    ╚═════════════════════════════════════════════════════╝
    """
    print(banner)


# Podman machine manager class with VM stop/start & compose up/down methods
class PodmanMachine:

    def __init__(self):
        pass

    def start(self):
        print("Starting podman VM:")

        subprocess.run(
            ["podman", "machine", "start"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        time.sleep(5)

    def stop(self):
        print("Stopping podman VM:")

        subprocess.run(
            ["podman", "machine", "stop"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

    def compose_up(self):
        print(f"Starting containers from: {COMPOSE_PATH}")
        print("Initilializing/running podman-compose up 'detached':")

        subprocess.run(
            ["podman-compose", "up", "-d"],
            cwd=COMPOSE_PATH,
        )

        print("\n✓ Started Containers!")

    def compose_down(self):
        print("Stopping containers:")

        subprocess.run(
            ["podman-compose", "down"],
            cwd=COMPOSE_PATH,
        )

        print("\n Stopped containers!")


def main():

    pm = PodmanMachine()

    while True:
        print_banner()
        os.system("podman machine list --format '{{.Name}}: {{.LastUp}}'")
        print("1.) Start VM")
        print("2.) Stop VM")
        print("3.) Start Containers")
        print("4.) Stop Containers")
        print("5.) Refresh")
        print("0.) EXIT")

        response = input("\nEnter the corresponding number:").strip()

        if response == "1":
            pm.start()
        elif response == "2":
            pm.stop()
        elif response == "3":
            pm.compose_up()
        elif response == "4":
            pm.compose_down()
        elif response == "5":
            time.sleep(0.5)
            continue
        elif response == "0":
            print("\nExitting App!")
            break
        else:
            print("\nTryAgain")


if __name__ == "__main__":
    main()

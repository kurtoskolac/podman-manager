import os
import time

# Docker compose YAML file path
COMPOSE_PATH = "~/Projects/self-hosted/docker-compose.yml"


# Print banner UI function
def print_banner():
    # 1.) Clear the screen
    # 2.) Print banner
    os.system("clear")

    banner = """

    ███████████████████████████████████████████████████████████████████
    █                                                                 █
    █  ██████╗  ██████╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗         █
    █  ██╔══██╗██╔═══██╗██╔══██╗████╗ ████║██╔══██╗████╗  ██║         █
    █  ██████╔╝██║   ██║██║  ██║██╔████╔██║███████║██╔██╗ ██║         █
    █  ██╔═══╝ ██║   ██║██║  ██║██║╚██╔╝██║██╔══██║██║╚██╗██║         █
    █  ██║     ╚██████╔╝██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║         █
    █  ╚═╝      ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝         █
    █                                                                 █
    █            ███╗   ███╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗███████╗
    █            ████╗ ████║██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝
    █            ██╔████╔██║███████║██║     ███████║██║██╔██╗ ██║█████╗  
    █            ██║╚██╔╝██║██╔══██║██║     ██╔══██║██║██║╚██╗██║██╔══╝  
    █            ██║ ╚═╝ ██║██║  ██║╚██████╗██║  ██║██║██║ ╚████║███████╗
    █            ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝
    █                                                                 █
    █        ███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗ 
    █        ████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗
    █        ██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝
    █        ██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
    █        ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║
    █        ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
    █                                                                 █
    █                   PMM: v 0.2                                    █
    █                                                                 █
    █                   Danijel Taric • 08/12/2025                    █
    █                                                                 █
    ███████████████████████████████████████████████████████████████████ 
    """
    print(banner)


# Podman machine manager class with VM stop/start & compose up/down methods
class PodmanMachine:

    def __init__(self):
        pass

    def start(self):
        print("Starting podman VM:")
        os.system("podman machine start > /dev/null 2>&1")
        time.sleep(5)

    def stop(self):
        print("Stopping podman VM:")
        os.system("podman machine stop > /dev/null 2>&1")

    def compose_up(self):
        print(f"Starting containers from: {COMPOSE_PATH}")
        print("Initilializing containers:")
        print("Running command: podman-compose up -d\n")
        os.system(f"cd {COMPOSE_PATH} && podman-compose up -d")
        print("\n✓ Command completed!")

    def compose_down(self):
        print("Stopping containers:")
        os.system(f"cd {COMPOSE_PATH} && podman-compose down")


def main():

    pm = PodmanMachine()

    while True:
        print_banner()
        os.system("podman machine list --format '{{.Name}}: {{.LastUp}}'")
        print("1.) Start VM")
        print("2.) Stop VM")
        print("3.) Start Containers")
        print("4.) Stop Containers")
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
        elif response == "0":
            print("\nExitting App!")
            break
        else:
            print("\nTryAgain")


if __name__ == "__main__":
    main()

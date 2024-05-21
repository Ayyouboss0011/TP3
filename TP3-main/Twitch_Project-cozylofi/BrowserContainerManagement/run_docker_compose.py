import subprocess
import time

def run_docker_compose():
    try:
        # Define the command
        command = ["docker-compose", "-f", "docker-compose1.yml", "up", "-d"]

        # Run the command
        subprocess.run(command, check=True)
        print("Docker Compose command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

    time.sleep(10)

    try:
        # Define the command
        command = ["docker-compose", "-f", "docker-compose2.yml", "up", "-d"]

        # Run the command
        subprocess.run(command, check=True)
        print("Docker Compose command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

    time.sleep(10)

    try:
        # Define the command
        command = ["docker-compose", "-f", "docker-compose3.yml", "up", "-d"]

        # Run the command
        subprocess.run(command, check=True)
        print("Docker Compose command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

    time.sleep(10)

    try:
        # Define the command
        command = ["docker-compose", "-f", "docker-compose4.yml", "up", "-d"]

        # Run the command
        subprocess.run(command, check=True)
        print("Docker Compose command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

    time.sleep(10)

    try:
        # Define the command
        command = ["docker-compose", "-f", "docker-compose5.yml", "up", "-d"]

        # Run the command
        subprocess.run(command, check=True)
        print("Docker Compose command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

    time.sleep(10)

    try:
        # Define the command
        command = ["docker-compose", "-f", "docker-compose6.yml", "up", "-d"]

        # Run the command
        subprocess.run(command, check=True)
        print("Docker Compose command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


    ###########################################################################################################
    
    
    # Kurze Wartezeit (10 Sekunden), um sicherzustellen, dass die Container gestartet wurden
    time.sleep(10)
    
    # Lösche alle temporären Volume Dateien
    try:
        subprocess.run(['docker', 'system', 'prune', '-a', '--volumes'], check=True, input='y', text=True)
        print("Cleanup successful.")
    except subprocess.CalledProcessError as e:
        print(f"Error cleaning up: {e}")

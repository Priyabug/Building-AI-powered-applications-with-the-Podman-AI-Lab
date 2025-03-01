# Import necessary libraries
import podman
import os

def create_podman_container(image_name, container_name):
    """
    Function to create and start a container using Podman image.
    :param image_name: The Docker or Podman image to use for the container
    :param container_name: Name to assign the new container
    :return: Container object
    """
    try:
        # Initialize Podman client
        client = podman.PodmanClient(base_url="unix:///run/podman/io.sock")

        # Create the container from the specified image
        container = client.containers.create(image_name, name=container_name)
        
        # Start the container
        container.start()
        print(f"Container '{container_name}' started successfully with image '{image_name}'.")
        
        return container
    except Exception as e:
        print(f"Error creating or starting container: {str(e)}")
        return None

def list_containers():
    """
    List all active Podman containers.
    """
    try:
        client = podman.PodmanClient(base_url="unix:///run/podman/io.sock")
        containers = client.containers.list()
        
        if containers:
            print("Active Containers:")
            for container in containers:
                print(f"- {container.name} (ID: {container.id})")
        else:
            print("No active containers found.")
    except Exception as e:
        print(f"Error listing containers: {str(e)}")

# Example usage of functions
if __name__ == "__main__":
    # Example: Create and run a container using an image
    image_name = "alpine"  # Use an image like 'alpine' for testing
    container_name = "test_container"
    
    # Create and start the container
    create_podman_container(image_name, container_name)
    
    # List active containers
    list_containers()

Description:
This project is designed to immerse students in the fundamentals of containerization and orchestration using Docker, Docker Compose, and GitHub Actions. Through a series of hands-on tasks, students will gain practical experience in creating, customizing, and deploying Docker images, managing data persistence, and orchestrating simple multi-service infrastructures. The project adopts a learn-by-doing approach, encouraging students to leverage provided resources, explore solutions independently, and collaborate to overcome challenges.

Objectives:
Understanding Containerization: Grasp the basics of containerization by creating and customizing Docker images based on the Alpine base image.
Automating Workflows: Learn how to automate the build and deployment of Docker images using GitHub Actions, fostering an understanding of CI/CD principles.
Managing Data Persistence: Explore the concept of data persistence in Docker by working with volumes to retain data across container restarts.
Exploring Orchestration: Dive into basic orchestration by setting up a simple infrastructure using Docker Compose, facilitating an understanding of multi-service deployments and inter-service communication.
Applying Best Practices: Implement best practices in Dockerfile creation, GitHub Actions workflow configuration, and Docker Compose setup to build a solid foundation for more complex projects.
Resources:
Please, be sure to watch the following introductory videos:

Containers and VMs - A Practical Comparison
What is a Container?
Containers 101
The following documentation will help you get a deeper understanding of the concepts:

Familiarize yourself with Docker by going through the Docker Official Documentation and Docker 101 Tutorial.
Learn about Docker Compose through the Docker Compose Documentation.
Look into Docker image creation on devopscube.com and linux.com.
Tasks
0. Create a Simple Docker Image Locally Based on Alpine
mandatory
Background:
Docker allows users to create lightweight and portable containers from custom images. One of the most lightweight base images used in Docker containers is Alpine, a security-oriented, lightweight Linux distribution.

Objective:
Create a Docker image using the Alpine base image. When a container is run using this image, it should print “Hello, World!” to the console.

Resources:
Docker documentation: https://docs.docker.com/
Alpine Docker image details: https://hub.docker.com/_/alpine
Instructions:
Setup:

Ensure Docker is installed on your machine.
Create a new directory for this project: mkdir docker-alpine-hello && cd docker-alpine-hello
Dockerfile:

In the project directory, create a file named Dockerfile.
Start the Dockerfile by specifying the Alpine base image using the FROM directive.
Use the CMD directive in the Dockerfile to echo “Hello, World!” when the container runs.
Building the Docker Image:

In your terminal or command line, navigate to the directory containing your Dockerfile.
Build the Docker image using the docker build command. Make sure to tag the image for easier reference:
 docker build -t hello-alpine .
Running the Docker Container:

Once the image is built, run a container from the image using the docker run command. If done correctly, you should see “Hello, World!” printed in your console.
 docker run hello-alpine
Notes:

Ensure you’re in the correct directory containing the Dockerfile when building the Docker image.
Double-check the syntax and directives in the Dockerfile to ensure the image builds without errors.
Hints:

The Dockerfile should be minimalistic, making use of the lightweight nature of the Alpine image.
Familiarize yourself with Docker’s CMD and ENTRYPOINT directives to understand which might be better suited for this task.
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: devops_essentials/docker-alpine-hello
File: Dockerfile
0/8 pts
1. Customize Your Alpine-based Docker Image
mandatory
Background:
Building on the foundation of the previous exercise, we’re now diving deeper into creating customized Docker images. By extending a Docker image, you can include additional tools and files, tailoring the container environment to your specific needs.

Objective:
Extend the Docker image created in the previous task to:

Install the curl package.
Add a configuration file named config.txt containing the text “Welcome to Docker!”.
When the Docker container is run, it should be able to execute curl commands. Additionally, the config.txt file should be accessible and contain the specified text.

Resources:
Docker documentation
Alpine package management
Instructions:
Setup:

Navigate to the directory of the previous task or create a new directory: mkdir docker-alpine-extended && cd docker-alpine-extended
Configuration File:

In the project directory, create a file named config.txt.
Add the text “Welcome to Docker!” to config.txt.
Dockerfile:

Modify or create a new Dockerfile.
Start with the same Alpine base image as the previous exercise.
Use the RUN directive to install the curl package. For Alpine, this would typically involve apk add --no-cache curl.
Use the COPY directive to add the config.txt file to a suitable location in the container, e.g., /app/config.txt.
Building the Docker Image:

Build the Docker image with the docker build command, and tag it appropriately:
 docker build -t extended-hello-alpine .
Testing the Docker Container:

Run a container from the newly created image.
Test the curl command by fetching a webpage, e.g., docker run extended-hello-alpine curl https://www.google.com.
Confirm the existence and content of the config.txt file, e.g., using docker run extended-hello-alpine cat /app/config.txt.
Notes:

Be cautious about the order of directives in the Dockerfile. The COPY command should come after the installation of necessary packages to make efficient use of Docker’s layer caching.
Hints:

Remember that each RUN, COPY, and ADD command creates a new layer in the Docker image. Use this to your advantage to ensure efficient builds, but also be mindful of the resulting image size.
Alpine’s package manager (apk) is different from those in Debian-based distributions (like apt). Ensure you’re using the correct commands for package management.
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: devops_essentials/docker-alpine-extended
File: Dockerfile, config.txt
0/10 pts
2. Automate Container Image Build and Push Using GitHub Actions
mandatory
Background:
Continuous integration (CI) is the practice of automating the integration of code changes from multiple contributors into a single software project. GitHub Actions is a platform that allows automation of workflows, including CI, directly within GitHub repositories. GitHub Container Registry is a feature provided by GitHub to host Docker containers.

Objective:
Set up a GitHub repository to store your Dockerfile. Implement a GitHub Actions workflow to:

Automatically build your Docker image when you push changes to your repository.
Push the built Docker image to the GitHub Container Registry.
Resources:
GitHub Actions documentation: https://docs.github.com/en/actions
GitHub Container Registry documentation: https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry
Instructions:
GitHub Repository:
Create a new GitHub repository to host your Dockerfile. You’ll use the Dockerfile from the previous task.
Clone the repository to your local machine and add your Dockerfile to it.
You’ll use this repository to test your workflow and for the MANUAL REVIEW. Provide the link to your repository on the URL form.

After that you can add the files to the Project repository specified in this task.

GitHub Actions Workflow: -Create a new file in the .github/workflows directory (you may need to create these directories). Name the file docker-image.yml.

Define a new workflow in this file. Use the on: push event to trigger the workflow on every push to the repository.
Define a job that does the following:
Checks out your repository.
Builds the Docker image.
Logs in to the GitHub Container Registry.
Pushes the Docker image to the registry.
GitHub Secrets:

For authentication with the GitHub Container Registry, you’ll need to use a token. In your repository, go to Settings > Secrets and create a new secret named CR_PAT that holds a Personal Access Token with the write:packages, read:packages, and delete:packages (if needed) scopes.
Notes:

The GitHub Container Registry requires Docker images to be tagged with a specific format. Ensure you follow the required naming conventions.
Ensure you use the GitHub Secrets appropriately in your workflow to avoid exposing sensitive information.
Hints:

Use GitHub’s marketplace to find pre-existing actions that help with Docker and container registry tasks, such as actions/checkout for checking out code and docker/login-action for logging into a container registry.
Always use secrets (never hard-code) for any tokens or sensitive information in GitHub Actions workflows.
Add URLs here:
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: devops_essentials/github_actions
File: docker-image.yml, Dockerfile
0/15 pts
3. Persist Data Using Volumes
mandatory
Background:
Docker volumes are a mechanism to persist data generated by and used by Docker containers. Unlike a bind mount, which mounts any directory from the host into the container, a volume is entirely managed by Docker. Volumes have several advantages over bind mounts, such as easier backup and migration, and are the preferred mechanism for persisting data generated by and used by Docker containers.

Objective:
Modify your existing Dockerfile to include a specified volume at /data. Demonstrate the persistence of data in this volume by:

Writing data to the volume.
Stopping the container.
Restarting the container.
Reading the data back from the volume to confirm its persistence.
Resources:
Docker Volumes documentation: https://docs.docker.com/storage/volumes/
Instructions:
Dockerfile Modification:

You’ll use your existing Dockerfile from the “Simple Docker Image” task.
Use the VOLUME directive to specify a volume at the /data path.
Building the Docker Image:

Build the Docker image with a suitable tag, e.g., docker build -t my-data-container ..
Running the Docker Container:

Run a container from the image, ensuring that you map a local directory to the /data volume for data persistence, e.g., docker run -v local_data_directory:/data my-data-container.
Demonstrating Data Persistence:

Write data to the volume, e.g., echo 'Hello, Docker Volumes!' > /data/hello.txt.
Stop the container using docker stop [container_id].
Restart the container using docker start [container_id].
Read the data back from the volume and confirm it matches the original data, e.g., cat /data/hello.txt.
Notes:

Ensure the local directory you map to the /data volume is kept consistent across container restarts to demonstrate persistence.
You might want to use a simple script or Docker command-line interface to write and read data for easier demonstration.
Hints:

Data written to volumes bypasses the container’s filesystem. This is what allows for the data to persist even after the container is stopped or deleted.
When demonstrating, take note of container IDs or names for accurate stopping and restarting.
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: devops_essentials/docker-volumes
File: Dockerfile
0/14 pts
4. Set Up a Simple Infrastructure Using Docker Compose
mandatory
Background
Docker Compose is a tool for defining and running multi-container Docker applications. For this exercise, students will work with PostgreSQL, a powerful open-source relational database, and pgAdmin, a popular open-source administration and management tool for the PostgreSQL database.

Objective
Define two services in a Docker Compose YAML file:

PostgreSQL: A relational database management system.
pgAdmin: A web-based administration tool for PostgreSQL.
The main goals are:

Set up a private network that both containers will use.
Allow public access only from the pgAdmin container.
Ensure pgAdmin can connect and manage the PostgreSQL database.
Explicitly configure the dependency between services, so the PostgreSQL container always starts before pgAdmin.
Resources:
Docker Compose documentation: https://docs.docker.com/compose/
PostgreSQL Docker image documentation: https://hub.docker.com/_/postgres
pgAdmin Docker image documentation: https://hub.docker.com/r/dpage/pgadmin4/
Instructions:
Setup:

Ensure Docker and Docker Compose are installed on your machine.
Create a new directory for this project: mkdir docker-pg-setup && cd docker-pg-setup
PostgreSQL:

You will be using the official Docker image for PostgreSQL. Make sure you understand the required environment variables to initialize a new database.
pgAdmin:

Similarly, you will use the official Docker image for pgAdmin. Understand how to configure the pgAdmin service to connect to the PostgreSQL instance.
Docker Compose:

In the root of your project directory, create a docker-compose.yml file.
Define two services: db and admin.
For the db service:
Use the official PostgreSQL Docker image.
Configure environment variables as necessary for initial setup.
Ensure the service is part of the private network.
For the admin service:
Use the official pgAdmin Docker image.
Set up necessary environment variables or configurations to ensure pgAdmin can connect to PostgreSQL.
Ensure the service is part of the private network.
Ensure this service depends on the db service using the depends_on field.
Define a custom private network and assign it to both services.
Make sure to expose only the necessary port(s) for pgAdmin to allow public access.
Execution:

Run the Docker Compose setup with: docker-compose up
Access pgAdmin via your browser on the exposed port. You should be able to connect and manage the PostgreSQL instance using the credentials provided in the Docker Compose file.
Notes:

Use Docker’s networking and service dependency features to make sure the two containers can communicate and that they start in the right order.
Make sure to handle potential database authentication issues, especially when setting up the pgAdmin connection to PostgreSQL.
Hints:

PostgreSQL default port is 5432, so ensure your pgAdmin configuration targets this port for database operations within the private network.
Remember to specify a volume for PostgreSQL if you want the data to persist across container restarts.
Look into Docker’s networks configuration for creating a private network.
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: devops_essentials/docker-compose
File: docker-compose.yml
0/20 pts

**surviving** STILL FIXING README ...

Alpine-based Docker image (Task 0):

Created Dockerfile in docker-alpine-hello directory.
Used Alpine base image.
Configured the container to print "Hello, World!".
Extended Alpine-based Docker image (Task 1):

Created Dockerfile and config.txt in docker-alpine-extended directory.
Extended the Alpine-based image to include the curl package.
Added a configuration file config.txt.
Automate Container Image Build and Push Using GitHub Actions (Task 2):

Created docker-image.yml workflow file in .github/workflows directory.
Set up a workflow to build and push Docker images to GitHub Container Registry.
Persist Data Using Volumes (Task 3):

Created Dockerfile in docker-volumes directory.
Configured a volume at /data path to persist data.
Demonstrated data persistence using a simple message written to the volume.
Set Up a Simple Infrastructure Using Docker Compose (Task 4):

Created docker-compose.yml in docker-compose directory.
Defined services for PostgreSQL and pgAdmin.
Configured a private network and volumes for PostgreSQL data persistence.
Ensured pgAdmin can connect and manage the PostgreSQL instance.

_______________________________________________

**docker-alpine-hello**:

    - Dockerfile exists and prints "Hello, World!" using Alpine.

**docker-alpine-extended**:

    - Dockerfile exists, installs curl, and adds `config.txt`
	 with the message "Welcome to Docker!".

    - `config.txt` exists and contains the text "Welcome to Docker!".

**github_actions**:

    - `.github/workflows/docker-image.yml` exists and
	 contains the correct workflow configuration
	 for building and pushing a Docker image.

**docker-volumes**:

    - Dockerfile exists and sets up a volume at `/data`.

**docker-compose**:

    - `docker-compose.yml` exists and defines services for
	 PostgreSQL and pgAdmin, with the necessary
	 configuration for networking and dependencies.



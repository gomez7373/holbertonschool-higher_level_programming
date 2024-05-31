# Docker Image Build and Push

This GitHub Actions workflow automatically builds a Docker image and pushes it to the GitHub Container Registry (GHCR) when code changes are pushed to the main branch.

## Usage

### Docker Image
- Build the Docker image locally:
  ```
  docker build -t <image_name> .
  ```
- Run the Docker container:
  ```
  docker run -it <image_name>
  ```

### GitHub Actions Workflow
- Push your code changes to the main branch.
- GitHub Actions will automatically build the Docker image and push it to GHCR.

For more details, refer to the [GitHub Actions workflow file](./.github/workflows/docker-image.yml).

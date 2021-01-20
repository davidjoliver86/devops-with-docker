# Dockerizer

This script clones a project from GitHub, builds it from the Dockerfile, and pushes the
image to Docker Hub.

## Usage
```
dockerizer.py [-h] [--docker-password DOCKER_PASSWORD] [--tag TAG] project docker_repo
```
* `project` - URL of the Git repo to clone the project (required).
* `docker_repo` - Repository for the image; should be in the format of `<hub-user>/<repo-name>` (required).
* `docker-password` - Your Docker Hub password. If not provided, it assumes you've already logged in.
* `tag` - Tag for the image (default: `latest`).

## Run in a container

By bind-mounting your existing `docker.sock`, you can run this in a container itself.
```
docker run --rm -it -v /var/run/docker.sock:/var/run/docker.sock dockerizer <args>
```
Or:
```
docker-compose run --rm dockerizer <args>
```

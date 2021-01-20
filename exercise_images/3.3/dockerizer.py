import os
import argparse
import tempfile
import subprocess
import contextlib
from typing import Optional


def _get_full_image_name(repo: str, tag: str):
    return f"{repo}:{tag}"


def clone_project(temp_dir: str, project_url: str):
    args = ["git", "clone", project_url, temp_dir]
    subprocess.run(args, check=True)


def build(temp_dir: str, image_ref: str):
    args = [
        "docker",
        "build",
        "-t",
        image_ref,
        temp_dir,
    ]
    subprocess.run(args, check=True)


def push_to_dockerhub(image_ref: str, password: Optional[str]):
    username = image_ref.split("/")[0]
    # Login if password provided; if not, assume you're already logged in
    if password:
        print("* Password provided; attempting to login")
        login_args = ["docker", "login", "--username", username, "--password", password]
        subprocess.run(login_args, check=True)
    else:
        print("* No password provided; assuming you've already logged in")
    push_args = ["docker", "push", image_ref]
    subprocess.run(push_args, check=True)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "project", type=str, help="URL of a Git repo containing a project"
    )
    parser.add_argument(
        "docker_repo",
        type=str,
        help="Dockerhub repo for your image",
        default=os.environ.get("DOCKER_REPO_NAME"),
    )
    parser.add_argument(
        "--docker-password",
        type=str,
        help="Docker hub password; if not provided, will assume you are logged in to Docker Hub",
        default=os.environ.get("DOCKER_PASSWORD"),
    )
    parser.add_argument(
        "--tag",
        type=str,
        help="Tag for the new image",
        default=os.environ.get("DOCKER_IMAGE_TAG", "latest"),
    )
    return parser.parse_args()


def main():
    args = parse_args()
    with tempfile.TemporaryDirectory() as td:
        image_ref = _get_full_image_name(args.docker_repo, args.tag)
        print(f"* Cloning {args.project} to {td}")
        clone_project(td, args.project)

        print(f"* Building {image_ref} from {td}")
        build(td, image_ref)

        print(f"* Pushing {image_ref} to Docker Hub")
        push_to_dockerhub(image_ref, args.docker_password)

        print("* Done")


if __name__ == "__main__":
    main()

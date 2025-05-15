#!/usr/bin/env python3
"""
Container management script for Docker Compose environments.

Provides commands to start, enter, and stop Docker Compose containers for
streamlined development workflows.
"""

import argparse
import subprocess
import sys


def run_cmd(cmd):
    """
    Run a shell command with error handling.

    Args:
        cmd (list): The command to run as a list of strings.
    """
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Command failed: {' '.join(cmd)}")
        sys.exit(e.returncode)


def start_container():
    """
    Start the Docker Compose environment in detached mode.
    """
    print("[INFO] Starting container in detached mode...")
    run_cmd(["docker", "compose", "up", "-d"])


def enter_container(service):
    """
    Enter the shell of the specified container.

    Args:
        service (str): The name of the Docker Compose service to enter.
    """
    print(f"[INFO] Entering container shell for service '{service}'...")
    run_cmd(["docker", "compose", "exec", service, "bash"])


def stop_container():
    """
    Stop and remove the running Docker Compose environment.
    """
    print("[INFO] Stopping and removing container...")
    run_cmd(["docker", "compose", "down"])


def main():
    """
    Command-line interface for managing Docker Compose containers.
    """
    parser = argparse.ArgumentParser(description="Manage Docker Compose containers.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # start
    subparsers.add_parser("start", help="Start the container in detached mode")

    # enter
    enter_parser = subparsers.add_parser("enter", help="Enter container shell")
    enter_parser.add_argument("--service", default="ai", help="Service name (default: ai)")

    # stop
    subparsers.add_parser("stop", help="Stop and remove the container")

    args = parser.parse_args()

    if args.command == "start":
        start_container()
    elif args.command == "enter":
        enter_container(args.service)
    elif args.command == "stop":
        stop_container()


if __name__ == "__main__":
    main()

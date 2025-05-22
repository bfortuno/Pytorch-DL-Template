#!/usr/bin/env python3
"""
Container management script for Docker Compose environments.

Supports starting, entering, and stopping Docker Compose containers,
with optional rebuild on start.
"""

import argparse
import subprocess
import sys
import shutil


def run_cmd(cmd, capture_output=False):
    """
    Run a shell command with optional output capture.

    Args:
        cmd (list): Command to run.
        capture_output (bool): Capture stdout if True.

    Returns:
        str: Output if capture_output is True, otherwise None.
    """
    try:
        if capture_output:
            result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return result.stdout.strip()
        else:
            subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Command failed: {' '.join(cmd)}")
        print(e.stderr if hasattr(e, 'stderr') else "")
        sys.exit(e.returncode)


def container_running(service):
    """
    Check if the given Docker Compose service is running.

    Args:
        service (str): Service name.

    Returns:
        bool: True if running, False otherwise.
    """
    output = run_cmd(["docker", "compose", "ps", "-q", service], capture_output=True)
    return bool(output)


def start_container(build=False):
    """
    Start the Docker Compose environment.

    Args:
        build (bool): Whether to rebuild the container.
    """
    cmd = ["docker", "compose", "up", "-d"]
    if build:
        cmd.append("--build")
        print("[INFO] Building and starting containers...")
    else:
        print("[INFO] Starting containers...")

    run_cmd(cmd)


def enter_container(service):
    """
    Enter the shell of a running container.

    Args:
        service (str): Service name.
    """
    if not container_running(service):
        print(f"[ERROR] Service '{service}' is not running.")
        sys.exit(1)

    # Try bash, fallback to sh
    shell = "bash" if shutil.which("bash") else "sh"
    print(f"[INFO] Entering '{service}' with shell: {shell} ...")
    try:
        run_cmd(["docker", "compose", "exec", service, shell])
    except SystemExit:
        if shell == "bash":
            print("[WARN] bash not available, retrying with sh...")
            run_cmd(["docker", "compose", "exec", service, "sh"])


def stop_container():
    """
    Stop and remove the Docker Compose environment.
    """
    print("[INFO] Stopping and removing containers...")
    run_cmd(["docker", "compose", "down"])


def main():
    parser = argparse.ArgumentParser(description="Manage Docker Compose containers.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Start
    parser_start = subparsers.add_parser("start", help="Start containers (optionally rebuild)")
    parser_start.add_argument("--build", action="store_true", help="Rebuild containers before starting")

    # Enter
    parser_enter = subparsers.add_parser("enter", help="Enter a running container's shell")
    parser_enter.add_argument("--service", default="ai", help="Service name (default: ai)")

    # Stop
    subparsers.add_parser("stop", help="Stop and remove containers")

    args = parser.parse_args()

    if args.command == "start":
        start_container(build=args.build)
    elif args.command == "enter":
        enter_container(args.service)
    elif args.command == "stop":
        stop_container()


if __name__ == "__main__":
    main()

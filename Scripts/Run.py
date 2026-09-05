#!/usr/bin/env python3
"""
sandbox_runner.py
A lightweight Python wrapper that executes a Vercel Sandbox command.

This mirrors the CLI pattern:
    npx sandbox login
    npx sandbox run --name "my-sandbox-001" --scope "ai-research" --network-policy deny-all --stop -- node -e "console.log('Hello from a sandbox')"
"""

import subprocess
import sys


def run_cmd(cmd: list[str]) -> int:
    """Run a shell command and stream output."""
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    for line in process.stdout:
        print(line, end="")

    for line in process.stderr:
        print(line, end="")

    return process.wait()


def sandbox_login() -> None:
    """Authenticate with Vercel Sandboxes."""
    print("🔐 Logging into Vercel Sandboxes…")
    code = run_cmd(["npx", "sandbox", "login"])
    if code != 0:
        print(f"Login failed with exit code {code}")
        sys.exit(code)


def sandbox_run() -> None:
    """Run a simple Node.js script inside a sandbox."""
    print("🚀 Starting sandbox execution…")

    cmd = [
        "npx", "sandbox", "run",
        "--name", "my-sandbox-001",
        "--scope", "ai-research",
        "--network-policy", "deny-all",
        "--stop",
        "--",
        "node", "-e", "console.log('Hello from a sandbox')"
    ]

    code = run_cmd(cmd)
    if code != 0:
        print(f"Sandbox run failed with exit code {code}")
        sys.exit(code)


def main():
    sandbox_login()
    sandbox_run()
    print("✨ Sandbox execution complete.")


if __name__ == "__main__":
    main()

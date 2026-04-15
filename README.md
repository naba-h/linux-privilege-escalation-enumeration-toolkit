#!/usr/bin/env python3
"""
Linux Privilege Escalation Enumeration Toolkit
---------------------------------------------

A clean, Pythonic CLI tool for identifying privilege escalation vectors.
Designed with simplicity, clarity, and practical usage in mind.
"""

from pathlib import Path
import os
import subprocess
import argparse
import json
from datetime import datetime

from rich.console import Console
from rich.table import Table

console = Console()


# ---------------------- Core Utilities ---------------------- #

def run(command: str) -> str:
    """Execute a shell command and return output."""
    try:
        return subprocess.check_output(
            command, shell=True, text=True, stderr=subprocess.DEVNULL
        ).strip()
    except subprocess.CalledProcessError:
        return ""


# ---------------------- Enumeration ---------------------- #

def get_system_info() -> dict:
    """Collect basic system information."""
    return {
        "user": run("whoami"),
        "hostname": run("hostname"),
        "kernel": run("uname -a"),
    }


def find_suid_binaries() -> list[str]:
    """Find SUID binaries."""
    output = run("find / -perm -4000 2>/dev/null")
    return output.splitlines() if output else []


def find_writable_paths(root: str = "/") -> list[str]:
    """Find writable files and directories."""
    writable = []
    for path in Path(root).rglob("*"):
        try:
            if os.access(path, os.W_OK):
                writable.append(str(path))
        except (PermissionError, OSError):
            continue
    return writable


# ---------------------- Output ---------------------- #

def display_system_info(info: dict):
    table = Table(title="System Information")
    table.add_column("Key", style="cyan")
    table.add_column("Value", style="green")

    for k, v in info.items():
        table.add_row(k, v)

    console.print(table)


def display_list(title: str, items: list[str], limit: int = 10):
    if not items:
        return

    console.print(f"\n[bold cyan][+] {title}[/bold cyan]")
    for item in items[:limit]:
        console.print(f"  [green]- {item}[/green]")


def save_report(data: dict, filename: str):
    """Save results to JSON file."""
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    console.print(f"\n[bold green]Report saved to {filename}[/bold green]")


# ---------------------- Main ---------------------- #

def main():
    parser = argparse.ArgumentParser(
        description="Linux Privilege Escalation Enumeration Toolkit"
    )
    parser.add_argument(
        "--json", help="Save output to JSON file", default=None
    )
    parser.add_argument(
        "--limit", help="Limit output results", type=int, default=10
    )

    args = parser.parse_args()

    console.print("[bold cyan][*] Starting enumeration...[/bold cyan]\n")

    system = get_system_info()
    suid = find_suid_binaries()
    writable = find_writable_paths()

    # Display
    display_system_info(system)
    display_list("SUID binaries detected", suid, args.limit)
    display_list("Writable files detected", writable, args.limit)

    console.print("\n[bold cyan][*] Enumeration complete.[/bold cyan]")

    # Save JSON if requested
    if args.json:
        report = {
            "timestamp": str(datetime.now()),
            "system": system,
            "suid": suid,
            "writable": writable,
        }
        save_report(report, args.json)


if __name__ == "__main__":
    main()

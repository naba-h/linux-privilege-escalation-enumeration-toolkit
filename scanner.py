
#!/usr/bin/env python3

import os
from datetime import datetime

# Colors for professional output
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

# Banner
def banner():
    print("="*70)
    print(BLUE + " Linux Privilege Escalation Enumeration Framework " + RESET)
    print(BLUE + " Automated Security Enumeration Toolkit " + RESET)
    print("="*70)
    print("Scan Time:", datetime.now())
    print("="*70)

# System Information
def system_info():
    print(YELLOW + "\n[INFO] System Information" + RESET)
    os.system("whoami")
    os.system("uname -a")
    os.system("id")

# Kernel Version
def kernel_version():
    print(YELLOW + "\n[INFO] Kernel Version" + RESET)
    os.system("uname -r")

# SUID Scan
def suid_scan():
    print(RED + "\n[HIGH] Scanning SUID Binaries" + RESET)
    os.system("find / -perm -4000 -type f 2>/dev/null")

# SGID Scan
def sgid_scan():
    print(RED + "\n[HIGH] Scanning SGID Binaries" + RESET)
    os.system("find / -perm -2000 -type f 2>/dev/null")

# World Writable Files
def writable_files():
    print(RED + "\n[HIGH] Searching World Writable Files" + RESET)
    os.system("find / -type f -perm -o+w 2>/dev/null")

# Writable Directories
def writable_dirs():
    print(RED + "\n[HIGH] Searching Writable Directories" + RESET)
    os.system("find / -type d -perm -o+w 2>/dev/null")

# Sudo Privileges
def sudo_check():
    print(YELLOW + "\n[MEDIUM] Checking Sudo Privileges" + RESET)
    os.system("sudo -l")

# Cron Jobs
def cron_jobs():
    print(YELLOW + "\n[MEDIUM] Checking Cron Jobs" + RESET)
    os.system("cat /etc/crontab")

# Linux Capabilities
def capabilities():
    print(YELLOW + "\n[MEDIUM] Checking Linux Capabilities" + RESET)
    os.system("getcap -r / 2>/dev/null")

# PATH Variable
def path_check():
    print(YELLOW + "\n[INFO] PATH Environment Variable" + RESET)
    os.system("echo $PATH")

# /etc/passwd Permissions
def passwd_check():
    print(YELLOW + "\n[INFO] Checking /etc/passwd Permissions" + RESET)
    os.system("ls -l /etc/passwd")

# /etc/shadow Permissions
def shadow_check():
    print(YELLOW + "\n[INFO] Checking /etc/shadow Permissions" + RESET)
    os.system("ls -l /etc/shadow")

# Home Directory Permissions
def home_permissions():
    print(YELLOW + "\n[INFO] Checking Home Directory Permissions" + RESET)
    os.system("ls -ld /home/*")

# Running Processes
def running_processes():
    print(YELLOW + "\n[INFO] Running Processes" + RESET)
    os.system("ps aux | head")

# Environment Variables
def environment_variables():
    print(YELLOW + "\n[INFO] Environment Variables" + RESET)
    os.system("env")

# Report Generation
def generate_report():
    with open("report.txt", "w") as report:
        report.write("Linux Privilege Escalation Scan Report\n")
        report.write("="*60 + "\n")
        report.write("Scan completed at: " + str(datetime.now()) + "\n")
        report.write("This report contains system enumeration results.\n")

# Main Execution
def main():

    banner()

    system_info()
    kernel_version()

    suid_scan()
    sgid_scan()

    writable_files()
    writable_dirs()

    sudo_check()
    cron_jobs()

    capabilities()
    path_check()

    passwd_check()
    shadow_check()

    home_permissions()
    running_processes()
    environment_variables()

    generate_report()

    print(GREEN + "\n[INFO] Security Enumeration Completed Successfully" + RESET)
    print("="*70)

if __name__ == "__main__":
    main()

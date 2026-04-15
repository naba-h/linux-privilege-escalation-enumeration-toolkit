Linux Privilege Escalation Enumeration Toolkit

A lightweight Python-based Linux security enumeration toolkit developed to assist penetration testers, security analysts, and cybersecurity students in identifying potential privilege escalation vectors in Linux environments.

This toolkit automates the discovery of system information, permission misconfigurations, and security weaknesses that may allow attackers to escalate privileges during the post-exploitation phase of penetration testing.

---

Project Overview

Privilege escalation is one of the most critical stages during a penetration testing engagement.
After gaining initial access to a system, attackers attempt to elevate their privileges in order to obtain administrative or root access.

The Linux Privilege Escalation Enumeration Toolkit automates the enumeration process by scanning Linux systems for potential security weaknesses that may lead to privilege escalation.

The toolkit performs checks for:

- SUID and SGID binaries
- Writable files and directories
- Cron job configurations
- Sudo privileges
- Linux capabilities
- System environment variables
- Kernel version information

These checks help security professionals quickly identify possible privilege escalation opportunities during security assessments.

---

Key Features

The toolkit performs automated enumeration of the following:

- System and user information
- Kernel version detection
- SUID binary discovery
- SGID binary detection
- World-writable file identification
- Writable directory discovery
- Cron job inspection
- Sudo privilege enumeration
- Linux capabilities detection
- Environment variable inspection

These security checks help identify misconfigurations and potential privilege escalation paths within Linux systems.

---

Project Structure

PrivEscToolkit
│
├── scanner.py
├── report.txt
├── README.md
└── screenshots/

scanner.py
Main Python script responsible for performing automated enumeration checks.

report.txt
Generated report containing the results of the security enumeration scan.

README.md
Project documentation explaining the tool and how to use it.

screenshots/
Contains screenshots demonstrating the tool execution and output.

---

Installation

Clone the repository:

git clone https://github.com/naba-h/linux-privilege-escalation-enumeration-toolkit.git

Navigate to the project directory:

cd linux-privilege-escalation-enumeration-toolkit

Verify Python installation:

python3 --version

---

Usage

Run the enumeration toolkit:

python3 scanner.py

Generate a detailed enumeration report:

python3 scanner.py > report.txt

The results of the enumeration scan will be saved in the report.txt file.

---

Enumeration Checks Performed

The toolkit automatically performs the following security checks:

- Current user and system information
- Kernel version analysis
- Detection of SUID binaries
- Detection of SGID binaries
- Identification of world-writable files
- Discovery of writable directories
- Sudo privilege inspection
- Cron job configuration analysis
- Linux capability enumeration
- Environment variable analysis

These techniques are widely used during the post-exploitation phase of penetration testing.

---

Example Use Case

During a penetration test, once an attacker gains initial access to a Linux system, enumeration is required to identify potential privilege escalation opportunities.

This toolkit helps automate that process by gathering system information and identifying possible attack vectors that may lead to privilege escalation.

---

Screenshots

Example tool execution:

"Tool Execution" (screenshots/tool_execution.png)

Example generated report:

"Scan Report" (screenshots/report_output.png)

---

Educational Purpose

This project was created for educational and cybersecurity learning purposes.
It demonstrates how automated scripts can assist in identifying security weaknesses and privilege escalation opportunities in Linux environments.

---

Author

Naba Hanfi
Cyber Security Enthusiast
Security Research Learner

---

Disclaimer

This project is intended strictly for educational purposes and authorized security testing only.

Do not use this tool on systems without proper permission.

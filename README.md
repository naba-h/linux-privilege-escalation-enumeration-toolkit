<h1 align="center">Linux Privilege Escalation Enumeration Toolkit</h1><p align="center">
A focused Python-based toolkit for identifying privilege escalation vectors in Linux systems.
</p><p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Status-Active-success?style=flat"/>
  <img src="https://img.shields.io/badge/License-MIT-2ea44f?style=flat"/>
  <img src="https://img.shields.io/badge/Maintained-Yes-blue?style=flat"/>
</p>---

Overview

Privilege escalation is often the most decisive phase of a security assessment. After initial access is obtained, the ability to elevate privileges determines the overall impact of the engagement.

This toolkit automates the enumeration process, systematically identifying misconfigurations, insecure permissions, and system artifacts that may lead to privilege escalation.

It is designed to provide a structured and repeatable workflow for both learners and security practitioners.

---

Demonstration

<p align="center">
  <img src="demo.gif" width="720"/>
</p>---

Core Capabilities

- Identification of SUID and SGID binaries
- Detection of writable files and directories
- Analysis of cron job configurations
- Enumeration of sudo privileges
- Inspection of Linux capabilities
- Environment variable analysis

---

Usage

python3 scanner.py

---

Installation

git clone https://github.com/naba-h/linux-privilege-escalation-enumeration-toolkit.git
cd linux-privilege-escalation-enumeration-toolkit

---

Sample Output

[+] Collecting system information...
[+] Checking SUID binaries...
[!] Potentially vulnerable binary identified

[+] Checking writable files...
[!] Writable path detected

[+] Checking sudo privileges...
[!] Misconfigured sudo permissions found

---

Architecture

.
├── scanner.py
├── report.txt
├── demo.gif
├── screenshots/
└── README.md

---

Design Principles

The toolkit is built with an emphasis on clarity, efficiency, and usability.

Rather than producing excessive output, it focuses on highlighting actionable findings — enabling faster analysis and decision-making during security assessments.

---

Practical Applications

- Penetration testing engagements
- Cybersecurity labs and training
- Capture The Flag (CTF) environments
- Linux security assessments

---

Disclaimer

This project is intended strictly for educational purposes and authorized security testing. Unauthorized use is prohibited.

---

Author

Naba Hanfi
https://github.com/naba-h

---

<p align="center">
If this project was useful, consider starring the repository.
</p>

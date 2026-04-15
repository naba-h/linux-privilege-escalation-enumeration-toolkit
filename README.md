<h1 align="center">Linux Privilege Escalation Enumeration Toolkit</h1><p align="center">
A minimal and practical toolkit to identify privilege escalation opportunities in Linux systems.
</p><p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Status-Active-success?style=flat"/>
  <img src="https://img.shields.io/badge/License-MIT-2ea44f?style=flat"/>
</p>---

✦ Overview

A lightweight Python-based enumeration tool designed to surface common misconfigurations and security weaknesses that may lead to privilege escalation.

Built with simplicity and clarity in mind — focusing on real-world usability rather than complexity.

---

✦ What it does

- Scans system-level configurations
- Identifies privilege escalation vectors
- Highlights insecure permissions
- Detects writable files and SUID binaries

---

✦ Quick Start

git clone https://github.com/naba-h/linux-privilege-escalation-enumeration-toolkit.git
cd linux-privilege-escalation-enumeration-toolkit
python3 scanner.py

---

✦ Demo

<p align="center">
  <img src="demo.gif" width="720"/>
</p>---

✦ Output Preview

[+] Collecting system information...
[+] Checking SUID binaries...
[!] Potential privilege escalation vector found

[+] Checking writable files...
[!] Writable file detected

[+] Enumeration complete.

---

✦ Structure

.
├── scanner.py
├── report.txt
├── demo.gif
├── screenshots/
└── README.md

---

✦ Why this exists

Manual enumeration is repetitive and error-prone.
This tool provides a consistent and automated way to identify security gaps during post-exploitation.

---

✦ Use Cases

- Security labs
- CTF challenges
- Linux hardening analysis
- Penetration testing practice

---

✦ Disclaimer

For educational use only.
Do not use without proper authorization.

---

✦ Author

Naba Hanfi
https://github.com/naba-h

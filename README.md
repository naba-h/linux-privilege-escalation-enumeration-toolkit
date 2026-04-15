<h1 align="center">Linux Privilege Escalation Enumeration Toolkit</h1>

<p align="center">
A focused Python-based toolkit for identifying privilege escalation vectors in Linux systems.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square"/>
  <img src="https://img.shields.io/badge/Maintained-Yes-blue?style=flat-square"/>
</p>

---

## 🔍 Overview

Privilege escalation is often the most critical phase in a security assessment.  
After gaining initial access, the ability to escalate privileges determines the overall impact of the engagement.

This toolkit automates the enumeration process by identifying:
- Misconfigured permissions  
- Insecure system files  
- Weak configurations  
- Potential privilege escalation vectors  

It is designed to provide a **structured, repeatable, and efficient workflow** for both learners and security professionals.

---

## ⚙️ Features

- 🔎 Automated privilege escalation checks  
- 📁 Detection of misconfigured files & directories  
- ⚠️ Identification of SUID/SGID binaries  
- 🧠 Simple and readable output  
- ⚡ Lightweight and fast execution  
- 🛠 Beginner-friendly and easy to modify  

---

## 🚀 Usage

```bash
git clone https://github.com/your-username/linux-privilege-escalation-enumeration-toolkit.git
cd linux-privilege-escalation-enumeration-toolkit
python3 scanner.py
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

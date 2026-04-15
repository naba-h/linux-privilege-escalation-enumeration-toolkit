<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&size=24&duration=3000&pause=1000&color=7AA2F7&center=true&vCenter=true&width=900&lines=Linux+Privilege+Escalation+Enumeration+Toolkit;Structured+Security+Enumeration;Built+for+Real+World+Usage" />
</p><p align="center">
  <sub style="color:#9aa5b1;">
  A structured Python toolkit for identifying privilege escalation opportunities in Linux systems.
  </sub>
</p><p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-7aa2f7?style=flat-square"/>
  <img src="https://img.shields.io/badge/Linux-Security-bb9af7?style=flat-square"/>
  <img src="https://img.shields.io/badge/Status-Active-7bd88f?style=flat-square"/>
  <img src="https://img.shields.io/badge/License-MIT-e0af68?style=flat-square"/>
</p>---

<p align="center">
  <img src="./demo.gif" width="780"/>
</p>---

<span style="color:#7aa2f7;">Overview</span>

Privilege escalation is one of the most critical stages in any security assessment.
Once initial access is obtained, identifying pathways to elevate privileges determines the true impact of the system compromise.

This project focuses on automating the enumeration phase, helping uncover misconfigurations and system weaknesses that could lead to privilege escalation.

It provides a consistent, repeatable, and efficient workflow that improves both accuracy and speed during analysis.

---

<span style="color:#bb9af7;">Problem Statement</span>

Manual enumeration in Linux environments can be:

- Time-consuming
- Inconsistent
- Easy to overlook critical misconfigurations

As a result, important privilege escalation vectors may remain undiscovered.

---

<span style="color:#7bd88f;">Solution Approach</span>

This toolkit automates the process by systematically scanning the system for:

- Misconfigured file permissions
- SUID/SGID binaries
- Writable files and directories
- Weak system configurations

The goal is to reduce manual effort while increasing coverage and reliability.

---

<span style="color:#e0af68;">Key Features</span>

- Automated privilege escalation enumeration
- Detection of insecure file permissions
- Identification of SUID/SGID binaries
- Clean, structured, and readable output
- Lightweight and efficient execution
- Easily extendable for custom use cases

---

<span style="color:#7aa2f7;">How It Works</span>

The script performs a sequence of checks across the system, including:

1. Collecting system-level information
2. Identifying privileged binaries
3. Scanning writable paths
4. Detecting misconfigurations

The output highlights potential escalation vectors for further analysis.

---

<span style="color:#bb9af7;">Usage</span>

git clone https://github.com/your-username/linux-privilege-escalation-enumeration-toolkit.git
cd linux-privilege-escalation-enumeration-toolkit
python3 scanner.py

---

<span style="color:#7bd88f;">Output</span>

The tool generates structured output that includes:

- System information
- SUID binaries
- Writable paths
- Potential privilege escalation findings

This allows quick identification of vulnerabilities without excessive noise.

---

<span style="color:#e0af68;">Project Structure</span>

.
├── scanner.py
├── report.txt
├── demo.gif
├── screenshots/
└── README.md

---

<span style="color:#bb9af7;">Use Cases</span>

- Penetration testing engagements
- Capture The Flag (CTF) challenges
- Cybersecurity learning and practice
- Linux misconfiguration analysis

---

<span style="color:#f7768e;">Disclaimer</span>

This project is intended strictly for educational and authorized security testing purposes only.
Unauthorized use is not permitted.

---

<span style="color:#7aa2f7;">Author</span>

<b style="color:#c0caf5;">Naba Hanfi</b>

---

<p align="center">
  <sub style="color:#565f89;">Designed with clarity, structure, and real-world application in mind.</sub>
</p>

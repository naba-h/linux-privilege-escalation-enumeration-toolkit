<h1 align="center">Linux Privilege Escalation Enumeration Toolkit</h1><p align="center">
A structured <b>Python-based toolkit</b> for identifying privilege escalation opportunities in Linux environments
</p><p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Linux-Security-555?style=flat-square&logo=linux"/>
  <img src="https://img.shields.io/badge/Status-Active-2ECC71?style=flat-square"/>
  <img src="https://img.shields.io/badge/License-MIT-F39C12?style=flat-square"/>
</p>---

<p align="center">
  <img src="./demo.gif" width="780"/>
</p>---

<span style="color:#00F7FF;">Overview</span>

Privilege escalation is often the stage that defines the true impact of a system compromise.
Once initial access is obtained, the ability to elevate privileges determines how far that access can extend.

In real-world environments, escalation paths are rarely obvious.
They are typically hidden within misconfigurations, weak permission models, and overlooked system artifacts.

This toolkit provides a structured and reliable approach to Linux enumeration, enabling consistent identification of potential escalation vectors.

Rather than relying on fragmented manual checks, it introduces a repeatable workflow focused on clarity and relevance.

---

<span style="color:#00F7FF;">Design Philosophy</span>

«Focus on meaningful signals — ignore unnecessary noise.»

The goal is not to generate more output, but to produce better, more actionable insights.

---

<span style="color:#00F7FF;">Core Capabilities</span>

The toolkit performs targeted analysis across key areas:

- Identification of SUID / SGID binaries
- Detection of writable files and directories
- Extraction of relevant system information
- Highlighting of potential privilege escalation paths
- Generation of clean and structured output

---

<span style="color:#00F7FF;">The Problem</span>

Manual enumeration is:

- time-consuming
- inconsistent
- dependent on individual experience
- prone to missing vulnerabilities

---

<span style="color:#00F7FF;">The Approach</span>

This tool standardizes the process through a clear pipeline:

1. System discovery
2. Permission analysis
3. Privilege indicator detection
4. Signal extraction

This ensures results remain focused, readable, and actionable.

---

<span style="color:#00F7FF;">Usage</span>

git clone https://github.com/your-username/linux-privilege-escalation-enumeration-toolkit.git
cd linux-privilege-escalation-enumeration-toolkit
python3 scanner.py

---

<span style="color:#00F7FF;">Example Output</span>

[+] System information collected
[+] SUID binaries detected
[!] Writable file found
[!] Potential privilege escalation path identified

---

<span style="color:#00F7FF;">Project Structure</span>

linux-privilege-escalation-enumeration-toolkit/
│
├── scanner.py           # Core logic
├── report.txt           # Output
├── demo.gif             # Demonstration
│
├── screenshots/
│   ├── output_1.png
│   ├── output_2.png
│   └── ...
│
└── README.md

---

<span style="color:#00F7FF;">Use Cases</span>

- Penetration testing
- Capture The Flag (CTF)
- Security learning
- Linux system analysis

---

<span style="color:#00F7FF;">Disclaimer</span>

This project is intended for educational purposes and authorized security testing only.

---

<span style="color:#00F7FF;">Author</span>

Naba Hanfi

---

<p align="center">
⭐ If you find this project useful, consider giving it a star
</p>

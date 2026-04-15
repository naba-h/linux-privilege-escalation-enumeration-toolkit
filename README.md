<h1 align="center">Linux Privilege Escalation Enumeration Toolkit</h1><p align="center">
A modern <b>Python-based security toolkit</b> for identifying privilege escalation vectors in Linux environments
</p><p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-7AA2F7?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Linux-Security-BB9AF7?style=flat-square&logo=linux"/>
  <img src="https://img.shields.io/badge/Focus-Privilege%20Escalation-7BD88F?style=flat-square"/>
  <img src="https://img.shields.io/badge/Status-Active-9ECE6A?style=flat-square"/>
  <img src="https://img.shields.io/badge/License-MIT-E0AF68?style=flat-square"/>
</p>---

<p align="center">
  <img src="./demo.gif" width="780" alt="Demo"/>
</p>---

<span style="color:#00F7FF;">Overview</span>

Privilege escalation is the phase that determines the true extent of system compromise.
Once initial access is established, the focus shifts from access to control — understanding how far that access can be extended.

In real-world systems, escalation vectors are rarely obvious. They typically emerge from:

- misconfigured permissions
- unsafe execution contexts
- overlooked system artifacts

This toolkit provides a structured, automated, and practical approach to Linux enumeration, enabling consistent identification of escalation opportunities.

---

<span style="color:#BB9AF7;">Core Idea</span>

«Identify what matters. Ignore everything else.»

The goal is to surface high-value signals, not overwhelm the user with unnecessary output.

---

<span style="color:#00F7FF;">Capabilities</span>

- Detection of SUID / SGID binaries
- Identification of writable files and directories
- Extraction of relevant system context
- Identification of misconfigurations and weak access controls
- Clean and structured output for analysis

---

<span style="color:#BB9AF7;">Why This Matters</span>

Manual enumeration is:

- time-consuming
- inconsistent
- dependent on experience
- prone to missing vulnerabilities

Missing a single signal can result in overlooking a complete escalation path.

---

<span style="color:#00F7FF;">Approach</span>

A simple and repeatable workflow:

1. Discover — collect system context
2. Analyze — evaluate permissions and configurations
3. Detect — identify privilege indicators
4. Extract — surface actionable findings

---

<span style="color:#BB9AF7;">Usage</span>

git clone https://github.com/your-username/linux-privilege-escalation-enumeration-toolkit.git
cd linux-privilege-escalation-enumeration-toolkit
python3 scanner.py

---

<span style="color:#00F7FF;">Example Output</span>

[+] System profile collected
[+] Privileged binaries identified
[!] Writable surface detected
[!] Escalation vector inferred

---

<span style="color:#BB9AF7;">Real-World Use</span>

With limited shell access, identifying escalation paths becomes critical.

This toolkit:

- automates enumeration
- highlights critical findings
- reduces the chance of oversight

Result: faster and more reliable security analysis.

---

<span style="color:#00F7FF;">Project Structure</span>

linux-privilege-escalation-enumeration-toolkit/
│
├── scanner.py           # Core enumeration logic
├── report.txt           # Output results
├── demo.gif             # Demonstration
│
├── screenshots/
│   ├── output_1.png
│   ├── output_2.png
│   └── ...
│
└── README.md

---

<span style="color:#BB9AF7;">Use Cases</span>

- penetration testing
- red team workflows
- Capture The Flag (CTF)
- cybersecurity learning

---

<span style="color:#F7768E;">Disclaimer</span>

This project is intended for educational purposes and authorized security testing only.

---

<span style="color:#7AA2F7;">Author</span>

Naba Hanfi

---

<p align="center">
⭐ If you find this project useful, consider giving it a star
</p><p align="center">
<sub>clean • structured • security-focused • Pythonic</sub>
</p>

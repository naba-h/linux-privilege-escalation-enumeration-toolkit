<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&size=24&duration=3000&pause=1000&color=89ddff&center=true&vCenter=true&width=900&lines=Linux+Privilege+Escalation+Enumeration+Toolkit;Where+Security+Meets+Precision;Designed+for+Real+World+Impact" />
</p><p align="center">
  <sub style="color:#9aa5b1;">
  A structured Python toolkit for identifying privilege escalation opportunities in Linux systems.
  </sub>
</p><p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-89ddff?style=flat-square"/>
  <img src="https://img.shields.io/badge/Linux-Security-c792ea?style=flat-square"/>
  <img src="https://img.shields.io/badge/Status-Active-a3be8c?style=flat-square"/>
  <img src="https://img.shields.io/badge/License-MIT-e5c07b?style=flat-square"/>
</p>---

<p align="center">
  <img src="./demo.gif" width="760"/>
</p>---

<span style="color:#89ddff;">Overview</span>

Privilege escalation is not just a step — it defines the impact of a security assessment.
Once initial access is obtained, the ability to elevate privileges determines how far control can be extended within a system.

This toolkit introduces a structured and automated approach to Linux enumeration, designed to uncover subtle misconfigurations and hidden system weaknesses.

It focuses on:

- Meaningful signals
- Relevant system artifacts
- Actionable findings

---

<span style="color:#c792ea;">Problem</span>

Manual enumeration is often:

- Time-consuming
- Inconsistent
- Prone to missing critical vulnerabilities

This creates gaps in identifying real privilege escalation opportunities.

---

<span style="color:#a3be8c;">Solution</span>

The toolkit automates enumeration by systematically identifying:

- Misconfigured permissions
- Writable files and directories
- SUID/SGID binaries
- Weak system configurations

This improves both efficiency and accuracy.

---

<span style="color:#e5c07b;">Approach</span>

The tool follows a structured workflow:

1. System discovery
2. Permission analysis
3. Privilege indicator detection
4. Signal extraction

This ensures a clear and focused output optimized for real-world usage.

---

<span style="color:#89ddff;">Usage</span>

git clone https://github.com/your-username/linux-privilege-escalation-enumeration-toolkit.git
cd linux-privilege-escalation-enumeration-toolkit
python3 scanner.py

---

<span style="color:#c792ea;">Example Output</span>

[+] System information collected
[+] SUID binaries detected
[!] Writable file found
[!] Potential privilege escalation path identified

---

<span style="color:#a3be8c;">Real-World Scenario</span>

Consider a system where an attacker has limited access.

Instead of manually checking configurations, this tool:

- Automates enumeration
- Highlights vulnerabilities
- Surfaces escalation paths

This significantly improves speed and reliability during assessments.

---

<span style="color:#e5c07b;">Before vs After</span>

Before

- Manual checks
- High effort
- Missed vulnerabilities

After

- Automated workflow
- Faster analysis
- Reliable and structured findings

---

<span style="color:#89ddff;">Project Structure</span>

.
├── scanner.py
├── report.txt
├── demo.gif
├── screenshots/
└── README.md

---

<span style="color:#c792ea;">Use Cases</span>

- Penetration testing
- Capture The Flag (CTF)
- Security learning
- Linux system analysis

---

<span style="color:#f7768e;">Disclaimer</span>

This project is intended strictly for educational and authorized security testing purposes only.

---

<span style="color:#89ddff;">Author</span>

Naba Hanfi

---

<p align="center">
  <sub style="color:#565f89;">
  Built with clarity, structure, and real-world application in mind.
  </sub>
</p>

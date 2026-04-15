<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&size=24&duration=3000&pause=1000&color=7AA2F7&center=true&vCenter=true&width=900&lines=Linux+Privilege+Escalation+Enumeration+Toolkit;Clean+Security+Automation;Built+for+Real+World+Usage" />
</p><p align="center">
  <sub style="color:#9aa5b1;">
  A modern Python toolkit for identifying privilege escalation opportunities in Linux systems.
  </sub>
</p><p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-7aa2f7?style=flat-square"/>
  <img src="https://img.shields.io/badge/Linux-Security-bb9af7?style=flat-square"/>
  <img src="https://img.shields.io/badge/Status-Active-7bd88f?style=flat-square"/>
  <img src="https://img.shields.io/badge/License-MIT-e0af68?style=flat-square"/>
</p>---

<p align="center">
  <img src="./demo.gif" width="760"/>
</p>---

<span style="color:#7aa2f7;">Overview</span>

«⚡ Designed to reduce manual enumeration effort and surface real privilege escalation vectors faster.
🎯 Built with a focus on clarity, signal over noise, and real-world usability.»

Privilege escalation defines the true impact layer of a security assessment.
Once initial access is obtained, identifying escalation paths determines how far control can be extended.

This toolkit provides a structured, automated, and practical approach to Linux enumeration, helping uncover misconfigurations and system weaknesses efficiently.

---

<span style="color:#bb9af7;">Key Features</span>

- Automated privilege escalation checks
- Detection of SUID / SGID binaries
- Identification of writable files and directories
- Structured and readable output
- Lightweight and easy to use

---

<span style="color:#7bd88f;">Problem</span>

Manual enumeration is:

- Time-consuming
- Inconsistent
- Easy to miss critical vulnerabilities

---

<span style="color:#e0af68;">Solution</span>

This tool automates enumeration by identifying:

- Misconfigured permissions
- Writable paths
- SUID/SGID binaries
- Weak system configurations

Result: faster and more reliable analysis

---

<span style="color:#7aa2f7;">Approach</span>

1. Collect system information
2. Analyze permissions
3. Detect privilege indicators
4. Highlight actionable findings

---

<span style="color:#bb9af7;">Usage</span>

git clone https://github.com/your-username/linux-privilege-escalation-enumeration-toolkit.git
cd linux-privilege-escalation-enumeration-toolkit
python3 scanner.py

---

<span style="color:#7bd88f;">Example Output</span>

[+] System information collected
[+] SUID binaries detected
[!] Writable file found
[!] Potential privilege escalation path identified

---

<span style="color:#e0af68;">Real-World Scenario</span>

With limited system access, manual checks are slow and error-prone.

This tool:

- Automates enumeration
- Surfaces key findings
- Reduces the chance of missing vulnerabilities

---

<span style="color:#7aa2f7;">Before vs After</span>

Before

- Manual checks
- High effort
- Missed signals

After

- Automated workflow
- Faster analysis
- Reliable results

---

<span style="color:#bb9af7;">Project Structure</span>

.
├── scanner.py
├── report.txt
├── demo.gif
├── screenshots/
└── README.md

---

<span style="color:#7bd88f;">Use Cases & Applications</span>

- Penetration testing
- Capture The Flag (CTF)
- Cybersecurity learning
- Linux system analysis

---

<span style="color:#f7768e;">Disclaimer</span>

This project is intended strictly for educational and authorized security testing purposes only.

---

<span style="color:#7aa2f7;">Author</span>

Naba Hanfi

---

<p align="center">
⭐ If you find this project useful, consider giving it a star!
</p><p align="center">
  <sub style="color:#565f89;">
  clean design — clear thinking — subtle <span style="color:#00f7ff;">neon light</span>
  </sub>
</p>

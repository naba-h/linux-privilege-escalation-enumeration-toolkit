<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&size=26&duration=2800&pause=800&color=00F7FF&center=true&vCenter=true&width=900&lines=Linux+Privilege+Escalation+Enumeration+Toolkit;Security+Focused+Automation;Signal+Over+Noise" />
</p><p align="center">
  <b>A structured Python toolkit designed to identify privilege escalation opportunities in Linux environments</b>
</p><p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-00f7ff?style=flat-square"/>
  <img src="https://img.shields.io/badge/Linux-Security-7aa2f7?style=flat-square"/>
  <img src="https://img.shields.io/badge/Focus-Enumeration-bb9af7?style=flat-square"/>
  <img src="https://img.shields.io/badge/Status-Active-7bd88f?style=flat-square"/>
</p>---

<p align="center">
  <img src="./demo.gif" width="780"/>
</p>---

<span style="color:#00F7FF;">Overview</span>

Privilege escalation is the stage that defines the true depth of system compromise.

After initial access is obtained, attackers — or security testers — attempt to expand their control by exploiting misconfigurations, weak permissions, or overlooked system artifacts.

This toolkit provides a structured, automated, and practical approach to Linux enumeration, enabling users to quickly identify potential escalation paths without relying on scattered manual checks.

It is built with one core principle:

«Focus on signal — ignore noise.»

---

<span style="color:#00F7FF;">Core Capabilities</span>

The tool performs targeted enumeration across critical areas:

- Detection of SUID / SGID binaries that may allow privilege abuse
- Identification of world-writable files and directories
- Extraction of system-level information relevant to escalation
- Highlighting of potential privilege escalation vectors
- Generation of clean, readable, and actionable output

---

<span style="color:#00F7FF;">Why This Matters</span>

Manual enumeration is often:

- Fragmented across multiple commands
- Time-intensive and repetitive
- Highly dependent on user experience
- Prone to missing subtle vulnerabilities

In real-world scenarios, these gaps can lead to overlooked escalation paths.

This tool addresses that problem by standardizing and automating the enumeration process, ensuring consistency and reliability.

---

<span style="color:#00F7FF;">Methodology</span>

The toolkit follows a clear and repeatable workflow:

1. System Discovery
   Collect essential system information

2. Permission Analysis
   Evaluate file and directory permissions

3. Privilege Indicator Detection
   Identify SUID/SGID binaries and risky configurations

4. Signal Extraction
   Highlight only the findings that matter

This structured approach ensures that results remain focused, relevant, and actionable.

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

<span style="color:#00F7FF;">Real-World Application</span>

Consider a scenario where a user gains limited shell access on a Linux system.

Instead of manually executing dozens of enumeration commands, this tool:

- Automates the discovery process
- Surfaces critical findings instantly
- Reduces the chance of missing escalation vectors

This significantly improves both efficiency and accuracy during security assessments.

---

<span style="color:#00F7FF;">Before vs After</span>

Before

- Manual enumeration
- High effort
- Inconsistent results
- Missed vulnerabilities

After

- Automated workflow
- Faster analysis
- Consistent output
- Reliable findings

---

<span style="color:#00F7FF;">Project Structure</span>

.
├── scanner.py
├── report.txt
├── demo.gif
├── screenshots/
└── README.md

---

<span style="color:#00F7FF;">Use Cases</span>

- Penetration testing engagements
- Capture The Flag (CTF) challenges
- Cybersecurity learning and practice
- Linux system security analysis

---

<span style="color:#00F7FF;">Disclaimer</span>

This project is intended strictly for educational and authorized security testing purposes only.

---

<span style="color:#00F7FF;">Author</span>

Naba Hanfi

---

<p align="center">
⭐ If you find this project useful, consider giving it a star
</p><p align="center">
<sub>security focused • structured approach • subtle neon precision</sub>
</p>

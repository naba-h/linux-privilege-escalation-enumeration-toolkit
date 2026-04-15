<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=28&duration=3000&pause=800&color=00F7FF&center=true&vCenter=true&width=900&lines=Linux+Privilege+Escalation+Enumeration+Toolkit;Automated+Security+Enumeration;Built+for+Pentesters+%26+Learners" />
</p><p align="center">
  <b style="color:#00F7FF;">⚡ Identify Privilege Escalation Vectors in Linux Systems ⚡</b>
</p><p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-7AA2F7?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Linux-Security-BB9AF7?style=for-the-badge&logo=linux"/>
  <img src="https://img.shields.io/badge/Status-Active-9ECE6A?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/License-MIT-E0AF68?style=for-the-badge"/>
</p>---

<p align="center">
  <img src="./demo.gif" width="820"/>
</p>---

<span style="color:#00F7FF;">Overview</span>

Privilege escalation represents a critical phase in any security assessment.
After initial access is obtained, the ability to elevate privileges determines the true scope and impact of system compromise.

In practical environments, escalation vectors are often non-obvious and embedded within:

- misconfigured permissions
- insecure file access controls
- weak system configurations
- overlooked system artifacts

This toolkit provides a structured and automated enumeration approach, enabling efficient identification of potential privilege escalation paths.

«⚡ Designed for clarity, efficiency, and real-world security workflows»

---

<span style="color:#BB9AF7;">Core Idea</span>

«Focus on high-value signals while minimizing unnecessary noise.»

The objective is to deliver concise, relevant, and actionable insights, rather than overwhelming users with excessive output.

---

<span style="color:#00F7FF;">Capabilities</span>

- Automated detection of privilege escalation vectors
- Identification of misconfigured permissions
- Analysis of SUID / SGID binaries
- Detection of writable files and directories
- Extraction of relevant system-level context
- Clean and structured output for analysis

---

<span style="color:#BB9AF7;">Why This Matters</span>

Manual enumeration is:

- time-intensive and repetitive
- dependent on individual expertise
- fragmented across multiple commands
- prone to missed vulnerabilities

These limitations increase the risk of overlooking critical escalation paths.

---

<span style="color:#00F7FF;">Approach</span>

The toolkit follows a clear and repeatable workflow:

1. System Discovery — collect environment context
2. Permission Analysis — evaluate access controls
3. Indicator Detection — identify privilege escalation signals
4. Signal Extraction — highlight actionable findings

This ensures results remain focused, consistent, and operationally useful.

---

<span style="color:#BB9AF7;">Quick Start</span>

git clone https://github.com/your-username/linux-privilege-escalation-enumeration-toolkit.git
cd linux-privilege-escalation-enumeration-toolkit
python3 scanner.py

---

<span style="color:#00F7FF;">Screenshots</span>

<p align="center">
  <img src="./screenshots/demo1.png" width="820"/>
</p>---

<span style="color:#BB9AF7;">Project Structure</span>

linux-privilege-escalation-enumeration-toolkit/
│
├── scanner.py           # Core enumeration engine
├── report.txt           # Generated output report
├── demo.gif             # Demonstration
│
├── screenshots/
│   └── demo1.png
│
└── README.md

---

<span style="color:#00F7FF;">Use Cases</span>

- penetration testing engagements
- Capture The Flag (CTF) challenges
- cybersecurity learning and practice
- Linux system security analysis

---

<span style="color:#F7768E;">Disclaimer</span>

This project is intended strictly for educational purposes and authorized security testing only.

---

<span style="color:#7AA2F7;">Author</span>

<b style="color:#00F7FF;">Naba Hanfi</b>
Cybersecurity • Python • Offensive Security

---

<p align="center">
🔥 <b>Star the repository if you find it useful</b> 🔥
</p>

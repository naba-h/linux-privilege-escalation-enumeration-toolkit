<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&size=24&duration=3000&pause=1000&color=7AA2F7&center=true&vCenter=true&width=900&lines=Linux+Privilege+Escalation+Enumeration+Toolkit;Clean+and+Structured+Security+Automation;Built+for+Practical+Use" />
</p><p align="center">
  <sub style="color:#9aa5b1;">
  A minimal, structured Python toolkit for identifying privilege escalation opportunities in Linux environments.
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

Privilege escalation is a defining phase in system security analysis.
After initial access, identifying reliable escalation paths determines the effectiveness of the assessment.

This project provides a clear and structured approach to Linux enumeration, focusing on uncovering misconfigurations and system weaknesses that may lead to privilege escalation.

The emphasis is on readability, consistency, and practical usefulness.

---

<span style="color:#bb9af7;">What This Tool Does</span>

The toolkit automates common enumeration tasks, including:

- Identifying SUID and SGID binaries
- Detecting writable files and directories
- Highlighting insecure permissions
- Surfacing potential escalation vectors

Each check is designed to produce concise and actionable output.

---

<span style="color:#7bd88f;">Design Principles</span>

- Keep output minimal and readable
- Focus on actionable findings
- Avoid unnecessary noise
- Maintain a predictable structure

The goal is to make results easy to interpret and useful in real workflows.

---

<span style="color:#e0af68;">Usage</span>

git clone https://github.com/your-username/linux-privilege-escalation-enumeration-toolkit.git
cd linux-privilege-escalation-enumeration-toolkit
python3 scanner.py

---

<span style="color:#7aa2f7;">Example Output</span>

[+] System Information
[+] SUID binaries identified
[!] Writable file detected
[!] Potential privilege escalation path found

---

<span style="color:#bb9af7;">Project Structure</span>

.
├── scanner.py
├── report.txt
├── demo.gif
├── screenshots/
└── README.md

---

<span style="color:#7bd88f;">Use Cases</span>

- Security assessments
- Capture The Flag (CTF) environments
- Cybersecurity learning
- Linux system analysis

---

<span style="color:#f7768e;">Disclaimer</span>

This project is intended for educational and authorized security testing only.

---

<span style="color:#7aa2f7;">Author</span>

<b style="color:#c0caf5;">Naba Hanfi</b>

---

<p align="center">
  <sub style="color:#565f89;">Simple, structured, and built for real use.</sub>
</p>

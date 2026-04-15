<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&size=26&duration=2800&pause=800&color=00F7FF&center=true&vCenter=true&width=900&lines=Linux+Privilege+Escalation+Enumeration+Toolkit;Security+Focused+Automation;Signal+Over+Noise" />
</p><p align="center">
  <b>A Python-based toolkit for systematically identifying privilege escalation opportunities in Linux environments</b>
</p><p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-00f7ff?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Linux-Security-0a0f2c?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Focus-Enumeration-00ffcc?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Active-00ff88?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/License-MIT-ffaa00?style=for-the-badge"/>
</p>---

<p align="center">
  <img src="./demo.gif" width="800"/>
</p>---

<span style="color:#00F7FF;">Overview</span>

Privilege escalation represents a critical phase in any security assessment.
After obtaining initial access, the ability to elevate privileges determines the true impact and depth of system compromise.

This project introduces a structured and automated enumeration framework designed to identify misconfigurations, weak permission models, and overlooked system artifacts within Linux environments.

Rather than relying on fragmented manual checks, this toolkit consolidates essential enumeration tasks into a single, efficient workflow.

«Core principle: Focus on meaningful signals while eliminating unnecessary noise.»

---

<span style="color:#00F7FF;">Problem Statement</span>

Manual enumeration in Linux systems is often:

- Time-consuming and repetitive
- Dependent on user expertise
- Fragmented across multiple commands
- Prone to missing subtle privilege escalation vectors

These limitations can lead to incomplete assessments and overlooked vulnerabilities.

---

<span style="color:#00F7FF;">Solution</span>

This toolkit automates the enumeration process by systematically identifying:

- SUID / SGID binaries that may allow privilege escalation
- Writable files and directories that can be exploited
- System-level configurations relevant to privilege escalation
- Hidden or indirect escalation paths

By standardizing these checks, the tool ensures consistency, accuracy, and reliability in security analysis.

---

<span style="color:#00F7FF;">Methodology</span>

The toolkit follows a clear, layered workflow:

1. System Discovery
   Collects essential system and environment information

2. Permission Analysis
   Evaluates file and directory permissions to identify weaknesses

3. Privilege Indicator Detection
   Detects SUID/SGID binaries and high-risk configurations

4. Signal Extraction
   Filters results to highlight only actionable findings

This approach ensures that the output remains focused, relevant, and actionable.

---

<span style="color:#00F7FF;">Key Features</span>

- Automated privilege escalation enumeration
- Detection of insecure file permissions
- Identification of SUID/SGID binaries
- Clean, structured, and readable output
- Lightweight and efficient execution
- Designed for real-world penetration testing workflows

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

Consider a scenario where a user gains limited shell access to a Linux system.

Instead of manually executing numerous enumeration commands, this toolkit:

- Automates the discovery process
- Surfaces critical findings immediately
- Reduces the likelihood of missing vulnerabilities

This significantly enhances both efficiency and accuracy during security assessments.

---

<span style="color:#00F7FF;">Before vs After</span>

Before

- Manual enumeration
- High effort and time consumption
- Inconsistent results
- Missed vulnerabilities

After

- Automated workflow
- Faster analysis
- Consistent and structured output
- Improved detection of escalation paths

---

<span style="color:#00F7FF;">Project Structure</span>

.
├── scanner.py          # Main enumeration script
├── report.txt          # Output report
├── demo.gif            # Demonstration
├── screenshots/        # Execution visuals
└── README.md

---

<span style="color:#00F7FF;">Use Cases</span>

- Penetration testing engagements
- Capture The Flag (CTF) challenges
- Cybersecurity training and learning
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
<sub>security focused • structured workflow • professional execution</sub>
</p>

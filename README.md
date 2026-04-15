<p align="center">
  <b>Linux Privilege Escalation Enumeration Toolkit</b>
</p><p align="center">
  <sub>
  A Python-based tool designed to systematically identify privilege escalation opportunities in Linux environments
  </sub>
</p>---

<span style="color:#00F7FF;">Overview</span>

Privilege escalation is a critical phase in any security assessment.
After gaining initial access, the ability to elevate privileges determines the true extent of system compromise.

In many cases, escalation paths are not obvious. They exist in the form of:

- misconfigured permissions
- insecure binaries
- overlooked system artifacts

This project addresses that challenge by providing a structured and automated enumeration process.

Instead of manually running multiple commands and risking missed vulnerabilities, this tool:

- consolidates key checks
- highlights relevant findings
- presents results in a clear and actionable format

«The core philosophy is simple: focus on meaningful signals, eliminate noise.»

---

<span style="color:#00F7FF;">Problem Statement</span>

Manual enumeration in Linux systems is:

- fragmented across many commands
- dependent on individual experience
- time-consuming and repetitive
- prone to human error

As a result, critical escalation paths are often overlooked during assessments.

---

<span style="color:#00F7FF;">Solution Approach</span>

This toolkit automates the enumeration process by systematically scanning the system for known escalation indicators.

It focuses on identifying:

- SUID / SGID binaries that may allow privilege abuse
- Writable files and directories that can be exploited
- System-level configurations relevant to escalation
- Hidden or indirect privilege escalation vectors

By standardizing these checks, the tool ensures consistency, coverage, and reliability.

---

<span style="color:#00F7FF;">How It Works</span>

The tool follows a step-by-step workflow:

1. System Discovery
   Collects essential system information such as environment details and configurations

2. Permission Analysis
   Evaluates file and directory permissions to identify weak access controls

3. Privilege Indicator Detection
   Detects SUID/SGID binaries and other high-risk elements

4. Signal Extraction
   Filters results to highlight only actionable findings

This layered approach ensures that output remains focused and useful, rather than overwhelming.

---

<span style="color:#00F7FF;">Key Features</span>

- Automated privilege escalation enumeration
- Detection of insecure permissions
- Identification of SUID/SGID binaries
- Clean, structured, and readable output
- Lightweight and easy to execute
- Designed for real-world usability

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

<span style="color:#00F7FF;">Real-World Scenario</span>

Consider a situation where an attacker or penetration tester gains limited shell access to a Linux system.

At this stage, identifying privilege escalation vectors becomes the priority.

Instead of manually executing dozens of enumeration commands, this tool:

- automates the discovery process
- surfaces critical findings immediately
- reduces the likelihood of missing vulnerabilities

This results in faster, more accurate, and more reliable assessments.

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
<sub>structured thinking • practical security • meaningful automation</sub>
</p>

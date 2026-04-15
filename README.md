<h1 align="center">Linux Privilege Escalation Enumeration Toolkit</h1><p align="center">
A structured <b>Python-based security toolkit</b> designed to systematically identify privilege escalation vectors in Linux environments
</p><p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Linux-Security-555?style=flat-square&logo=linux"/>
  <img src="https://img.shields.io/badge/Status-Active-2ECC71?style=flat-square"/>
  <img src="https://img.shields.io/badge/License-MIT-F39C12?style=flat-square"/>
</p>---

<p align="center">
  <img src="./demo.gif" width="750"/>
</p>---

<span style="color:#00F7FF;">Overview</span>

Privilege escalation constitutes a critical phase in any security assessment.
Following initial access, the capability to elevate privileges directly influences the scope, persistence, and impact of system compromise.

In real-world environments, escalation vectors are rarely explicit.
They are typically embedded within misconfigurations, weak permission models, or overlooked system artifacts.

This toolkit introduces a systematic and automated enumeration framework that enables security practitioners to efficiently identify such vectors with precision and consistency.

Rather than relying on fragmented manual techniques, it consolidates essential checks into a cohesive and repeatable workflow.

---

<span style="color:#00F7FF;">Design Philosophy</span>

The toolkit is built upon a fundamental principle:

«Prioritize high-signal findings while minimizing informational noise.»

The objective is to deliver concise, relevant, and actionable output, rather than overwhelming the user with excessive data.

---

<span style="color:#00F7FF;">Core Capabilities</span>

The tool performs targeted enumeration across critical system components:

- Identification of SUID / SGID binaries with potential privilege abuse implications
- Detection of world-writable files and directories
- Extraction of system-level context relevant to escalation analysis
- Identification of misconfigurations and weak access controls
- Generation of structured and human-readable output

---

<span style="color:#00F7FF;">Problem Statement</span>

Manual enumeration within Linux environments is inherently:

- Time-intensive and repetitive
- Dependent on operator expertise
- Fragmented across multiple commands and tools
- Susceptible to oversight and missed vulnerabilities

These limitations often result in incomplete or inconsistent security assessments.

---

<span style="color:#00F7FF;">Methodology</span>

The toolkit follows a clearly defined enumeration pipeline:

1. System Discovery
   Collection of foundational system and environment data

2. Permission Analysis
   Evaluation of file and directory access controls

3. Privilege Indicator Detection
   Identification of SUID/SGID binaries and high-risk configurations

4. Signal Extraction
   Filtering and prioritization of actionable findings

This structured approach ensures that results remain focused, relevant, and operationally useful.

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
[!] Potential privilege escalation vector identified

---

<span style="color:#00F7FF;">Operational Context</span>

Consider a scenario where limited shell access is obtained on a Linux host.

At this stage, identifying escalation vectors becomes a priority.

This toolkit:

- Automates the enumeration workflow
- Surfaces high-risk findings in real time
- Reduces the probability of missing critical escalation paths

As a result, it significantly enhances efficiency, accuracy, and reliability during security assessments.

---

<span style="color:#00F7FF;">Impact Analysis</span>

Before

- Manual enumeration processes
- High operational overhead
- Inconsistent output
- Increased risk of oversight

After

- Automated and structured workflow
- Reduced analysis time
- Consistent and reliable results
- Improved detection of escalation vectors

---

<span style="color:#00F7FF;">Project Structure</span>

.
├── scanner.py          # Core enumeration engine
├── report.txt          # Generated output report
├── demo.gif            # Demonstration
├── screenshots/        # Supporting visuals
└── README.md

---

<span style="color:#00F7FF;">Use Cases</span>

- Penetration testing engagements
- Capture The Flag (CTF) challenges
- Cybersecurity training and education
- Linux system security auditing

---

<span style="color:#00F7FF;">Disclaimer</span>

This project is intended strictly for educational purposes and authorized security assessments only.

---

<span style="color:#00F7FF;">Author</span>

Naba Hanfi

---

<p align="center">
⭐ If you find this project valuable, consider giving it a star
</p><p align="center">
<sub>precision • consistency • structured security analysis</sub>
</p>

# Suspicious Web Traffic Detection System

This project analyzes web server logs to detect suspicious or malicious activities such as admin page attacks, SQL injection attempts, and abnormal repeated requests. It generates a clear security report to help identify early signs of attacks.


# Project Overview

Web servers store every user request in log files. These logs contain hidden patterns that can reveal hacking attempts.  
This project reads a sample access.log file and automatically detects:

- Repeated access to /admin page  
- SQL Injection attempts (' OR 1=1 --)  
- Too many repeated requests from the same IP (bot-like behavior)  
- Any suspicious or abnormal access pattern  

All detected activities are saved into report.txt.

---

# What This Project Demonstrates

- Basic log analysis  
- Understanding of how attackers behave  
- Identifying suspicious HTTP traffic  
- Detecting common attack patterns  
- Simple incident reporting  
- Python scripting for security automation  

This aligns with real-world security operations roles.

---

# Technologies Used

- *Python* – for detecting suspicious patterns  
- *HTML* – simple website page for sample traffic  
- **Log File (access.log)** – contains raw web traffic  
- **Text Report (report.txt)** – final output of detected attacks  

---

## 📁 Project Structure

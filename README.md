# Cloud-Shadow 🌑 🏹

![Security](https://img.shields.io/badge/Security-Offensive-red.svg)
![Python](https://img.shields.io/badge/Python-3.x-yellow.svg)
![Recon](https://img.shields.io/badge/Recon-Cloud-blue.svg)

**Cloud-Shadow** is a high-speed infrastructure reconnaissance engine. It is engineered to identify exposed Cloud Metadata, DevOps secrets, and sensitive configuration leaks that automated enterprise scanners frequently overlook.

> **Research Note:** This tool is built for the "black-box" phase of Bug Bounty engagements where infrastructure transparency is the primary target.

---

## 🛑 ETHICAL & LEGAL NOTICE (MANDATORY)

**Usage of Cloud-Shadow for attacking targets without prior mutual consent is strictly prohibited.**
- This tool is for **authorized security auditing** and **educational purposes** only.
- The developer assumes **no liability** for any misuse or damage caused by this program.
- You must comply with all local and international laws regarding cyber security.
- **Unauthorized access is a crime.** Use your skills for good.

---

## ⚡ Technical Capabilities

* **Multi-Threaded Recon:** Utilizes a high-performance threading pool for rapid asset discovery.
* **Metadata Exfiltration:** Specific payloads for AWS, GCP, and Azure instance metadata services.
* **DevOps Leakage Hunter:** Targets CI/CD artifacts, `.env` files, `.git` directories, and Docker configs.
* **WAF Evasion:** Implements random User-Agent rotation and internal IP spoofing headers (`X-Forwarded-For`, etc.).
* **Status Code Intelligence:** Analyzes response sizes and codes (including 403/405) to map the hidden attack surface.

---

## 🚀 Deployment

```bash
# Clone the repository
git clone https://github.com/can0x01/Cloud-Shadow

# Enter the workspace
cd Cloud-Shadow

# Setup dependencies
pip3 install -r requirements.txt

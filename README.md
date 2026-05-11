# 🛡️ Pentesting-Resources

> **My personal Penetration Testing notes**  
> OWASP Top 10 • Real Labs • OSINT Scripts • Detailed Walkthroughs

[![OWASP](https://img.shields.io/badge/OWASP-Top%2010-red?style=for-the-badge)](https://owasp.org/www-project-top-ten/)
[![Made with ❤️](https://img.shields.io/badge/Made%20with-Love-red?style=for-the-badge)](https://github.com/mohamed-algabry)

---

## Table of Contents

- [About](#about)
- [Repository Structure](#repository-structure)
- [OWASP Top 10 Coverage](#owasp-top-10-coverage)
- [How to Use](#how-to-use)
- [Contributing](#contributing)
- [Contact](#contact)

---

## About

This repository contains my organized notes and practical labs for **Penetration Testing**, with special focus on the **OWASP Top 10 Web Application Security Risks**.

Every folder is named after a specific vulnerability or topic (following clean naming like the Web Security Academy style).

---

## Repository Structure

Pentesting-Resources/
├── broken-access-control/
├── broken-authentication/
├── sql-injection/
├── xss/
├── csrf/
├── ssrf/
├── command-injection/
├── directory-traversal/
├── file-upload-vulnerabilities/
├── information-disclosure/
├── jwt-attacks/
├── oauth-vulnerabilities/
├── xxe-injection/
├── websockets-vulnerabilities/
├── cors/
├── clickjacking/
├── business-logic-vulnerabilities/
├── dom-based-vulnerabilities/
├── http-host-header-attacks/
├── api-pentesting/
├── osint/                    ← OSINT Top 10 tools & scripts
├── privilege-escalation/
├── active-directory/
└── resources/                ← Cheat sheets & references


Each folder contains its own `README.md` with:
- Detailed explanation
- Attack steps
- Useful commands
- Notes & lessons learned

---

## OWASP Top 10 Coverage

| #  | Vulnerability                              | Folder                              | Status      |
|----|--------------------------------------------|-------------------------------------|-------------|
| 1  | Broken Access Control                      | `broken-access-control`             | ✅ Done     |
| 2  | Cryptographic Failures                     | `broken-authentication`             | ✅ Done     |
| 3  | Injection                                  | `sql-injection`, `command-injection`| In Progress |
| 4  | Insecure Design                            | `business-logic-vulnerabilities`    | Planned     |
| 5  | Security Misconfiguration                  | `information-disclosure`            | ✅ Done     |
| 6  | Vulnerable and Outdated Components         | `api-pentesting`                    | Planned     |
| 7  | Identification and Authentication Failures | `broken-authentication`             | ✅ Done     |
| 8  | Software and Data Integrity Failures       | `jwt-attacks`                       | ✅ Done     |
| 9  | Security Logging and Monitoring Failures   | `resources/`                        | Planned     |
| 10 | Server-Side Request Forgery (SSRF)         | `ssrf`                              | ✅ Done     |

---

## How to Use

```bash```
# Clone the repo
git clone https://github.com/mohamed-algabry/Pentesting-Resources.git
cd Pentesting-Resources

# Go to any topic
cd sql-injection
cat README.md

--

## Contact

GitHub: @mohamed-algabry
LinkedIn: Mohamed Algabry
X: @Jabry_00

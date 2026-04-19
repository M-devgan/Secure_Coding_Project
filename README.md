# Secure Coding Project – Code Security Audit

## 1. Project Overview
This project was developed as part of the Code Security Audit assignment. The objective of this project is to evaluate an existing application for potential security vulnerabilities and demonstrate the application of secure coding practices.

The project includes frontend components developed using HTML, CSS, and JavaScript, along with a Python script used for security analysis. Additionally, GitHub Actions workflows have been implemented to automate code quality checks and security scanning.

---

## 2. Objectives
The main objectives of this project are:
- To identify insecure coding practices within the application
- To map identified vulnerabilities to the OWASP Top 10 categories
- To implement automated tools for code quality and security analysis
- To recommend mitigation strategies based on industry best practices

---

## 3. Technologies Used
- HTML, CSS, JavaScript
- Python
- Git and GitHub
- GitHub Actions

---

## 4. Security Tools and Automation

### 4.1 Super-Linter
Super-Linter is used to enforce coding standards and improve code quality. It performs automated checks for syntax errors and formatting issues across multiple programming languages.

### 4.2 Bandit
Bandit is a Python-based security analysis tool that scans the source code for common security vulnerabilities, such as hardcoded credentials and unsafe function usage.

---

## 5. GitHub Workflows
The project utilizes GitHub Actions to automate continuous integration processes. The workflows are located in the following directory:

.github/workflows/

The following workflows have been implemented:
- super-linter.yml: Performs automated code linting and quality checks
- bandit.yml: Performs security analysis on Python files

These workflows are triggered automatically on push and pull request events.

---

## 6. Security Considerations
The project demonstrates potential security risks such as:
- Hardcoded sensitive information
- Use of unsafe system-level commands
- Lack of input validation

These issues are identified and analyzed as part of the security audit process.


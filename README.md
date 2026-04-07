# DevSecOps Vulnerable Flask Application

This project demonstrates a vulnerable Flask web application used to test DevSecOps CI/CD pipelines.

## Vulnerabilities

- SQL Injection
- Cross Site Scripting (XSS)
- Command Injection
- Hardcoded Secret
- Sensitive Information Exposure

## DevSecOps Tools

- GitHub Actions
- Bandit (SAST)
- Safety (Dependency Scan)
- Docker
- Trivy (optional)

## Run Locally

pip install -r requirements.txt
python app/app.py

Application runs on:
http://localhost:5000
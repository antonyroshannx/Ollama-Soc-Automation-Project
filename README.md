# CyberAI-SOC – AI-Powered Security Log Analysis & Automation

## Project Overview

CyberAI-SOC is a Python-based cybersecurity automation project that integrates a locally hosted Large Language Model (LLM) through Ollama to assist with security log analysis.

The project explores how AI can support Security Operations Center (SOC) workflows by processing security-related log information, identifying potentially suspicious activity, generating analytical explanations, and producing structured security reports.

The primary objective is to explore the integration of Python automation and local AI models in cybersecurity operations while maintaining data privacy through local model execution.

## Project Objectives

- Explore AI-assisted security log analysis.
- Automate repetitive log-analysis tasks using Python.
- Integrate a locally hosted LLM using Ollama.
- Generate understandable explanations of suspicious log activity.
- Support basic SOC investigation and documentation workflows.
- Explore privacy-conscious AI automation without relying on external hosted AI APIs.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Automation and log processing |
| Ollama | Local AI model execution |
| Llama 3.2 (3B) | Local language model |
| Requests | Python-to-Ollama API communication |
| Security Logs | Input for analysis |

## System Architecture

```text
        SECURITY LOGS
              |
              v
      PYTHON AUTOMATION
              |
       Log Processing
              |
              v
       OLLAMA LOCAL API
              |
              v
       LLAMA 3.2 (3B)
              |
       AI-ASSISTED ANALYSIS
              |
              v
       SECURITY REPORT
```

## Core Functionalities

### 1. Python Automation
- Reads security-related log information.
- Automates the communication between Python and Ollama.
- Sends relevant log information to the local AI model.
- Handles the AI response for further processing.

### 2. AI-Assisted SOC Analysis
- Examines supplied security log entries.
- Provides explanations of potentially suspicious activity.
- Helps interpret authentication-related events and unusual patterns.
- Supports preliminary security investigation.

### 3. Automated Reporting
- Generates readable security-analysis reports.
- Organizes AI-generated observations.
- Helps document potential security concerns and recommended investigation steps.

### 4. Local AI Integration
- Uses Ollama to run the language model locally.
- Communicates through the local Ollama API.
- Explores privacy-conscious AI-assisted security workflows.

## Project Structure

```text
CyberAI-SOC/
│
├── src/
│   └── analyzer.py
│
├── logs/
│   └── sample_logs.txt
│
├── reports/
│
├── screenshots/
│
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```

*Note: The structure and filenames should be adjusted to match the actual project files.*

## Installation & Setup

### Prerequisites
- Python 3.x
- Ollama
- Git
- Llama 3.2 (3B) model

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/CyberAI-SOC.git
cd CyberAI-SOC
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install the Ollama Model

```bash
ollama pull llama3.2:3b
```

### 5. Run Ollama

Ensure the Ollama service is running.

### 6. Execute the Python Application

```bash
python src/analyzer.py
```

*The execution command must be updated if your actual entry-point filename or location differs.*

## Security & Privacy Considerations

This repository is intended for educational and cybersecurity portfolio purposes.

To protect sensitive information:

- No real user credentials or passwords are included.
- No API keys, authentication tokens or private configuration files are published.
- Private IP addresses, hostnames and identifying information are replaced with placeholders where appropriate.
- Sample log files should contain synthetic or sanitized data.
- Sensitive investigation details and confidential reports are excluded.
- Local AI execution is used to explore privacy-conscious processing.

**Important:** Local AI execution does not automatically guarantee data security. Access to local logs, model storage and generated reports must still be protected.

## Project Limitations

- AI-generated analysis may contain inaccurate interpretations.
- Findings require human verification.
- The project is not a replacement for an enterprise SIEM.
- It does not independently guarantee attack detection or incident prevention.
- Results depend on the quality and context of supplied logs.

## Learning Outcomes

- Python-based cybersecurity automation.
- Local LLM integration using Ollama.
- Understanding SOC log-analysis workflows.
- AI-assisted security investigation.
- API communication and response handling.
- Security documentation and reporting.

## Disclaimer

This project is developed for educational, research and cybersecurity portfolio purposes. It should only be used with logs and systems that you are authorized to access.

AI-generated findings should be independently validated before being treated as confirmed security incidents.

## Author

**Antony Roshan N X**

Cybersecurity | Security Operations | Python Automation | AI-Assisted Security Research

GitHub: https://github.com/antonyroshannx

TryHackMe: https://tryhackme.com/p/antonyroshan

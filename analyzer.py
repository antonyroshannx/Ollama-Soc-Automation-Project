
import requests
from pathlib import Path
from datetime import datetime

# Project configuration
BASE_DIR = Path(__file__).resolve().parent.parent
LOG_FILE = BASE_DIR / "logs" / "sample_logs.txt"
REPORT_DIR = BASE_DIR / "reports"

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2:3b"


def read_logs():
    if not LOG_FILE.exists():
        raise FileNotFoundError(f"Log file not found: {LOG_FILE}")

    return LOG_FILE.read_text(encoding="utf-8")


def detect_suspicious_activity(logs):
    failed_count = logs.count("Failed Login")
    successful_count = logs.count("Successful Login")

    print("\n===== BASIC LOG ANALYSIS =====")
    print(f"Failed login events: {failed_count}")
    print(f"Successful login events: {successful_count}")

    if failed_count >= 3:
        print("Warning: Multiple failed login events detected.")

    return failed_count, successful_count


def analyze_with_llama(logs, failed_count, successful_count):
    prompt = f"""
You are a cybersecurity SOC analyst assistant.

Analyze these simulated Windows security logs.

Failed login events: {failed_count}
Successful login events: {successful_count}

Logs:
{logs}

Provide your analysis under these headings:
1. Summary
2. Suspicious Activity
3. Possible Security Risks
4. MITRE ATT&CK relevance, if applicable
5. Recommended Investigation Steps

Important:
Do not claim an attack is confirmed.
Clearly distinguish evidence from assumptions.
Do not recommend automatically blocking IP addresses.
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=300
    )

    response.raise_for_status()
    return response.json()["response"]


def save_report(analysis):
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    filename = datetime.now().strftime(
        "SOC_Report_%Y%m%d_%H%M%S.txt"
    )

    report_path = REPORT_DIR / filename

    report_path.write_text(
        analysis,
        encoding="utf-8"
    )

    return report_path


def main():
    print("CyberAI SOC - Local Log Analyzer")
    print("--------------------------------")

    try:
        logs = read_logs()

        failed, successful = detect_suspicious_activity(logs)

        print("\nSending logs to local Llama model...")

        analysis = analyze_with_llama(
            logs, failed, successful
        )

        print("\n===== AI SECURITY ANALYSIS =====")
        print(analysis)

        report_path = save_report(analysis)

        print(f"\nReport saved at: {report_path}")

    except requests.exceptions.ConnectionError:
        print("Error: Ollama is not running.")

    except requests.exceptions.RequestException as error:
        print(f"Ollama request failed: {error}")

    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()

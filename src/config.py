import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def load_settings() -> dict:
    api_url = os.getenv("ARBEITNOW_API_URL", "https://www.arbeitnow.com/api/job-board-api").strip()

    if not api_url:
        raise ValueError("ARBEITNOW_API_URL must not be empty.")

    try:
        timeout = float(os.getenv("REQUEST_TIMEOUT_SECONDS", "30"))
    except ValueError as error:
        raise ValueError("REQUEST_TIMEOUT_SECONDS must be a number.") from error

    if timeout <= 0:
        raise ValueError("REQUEST_TIMEOUT_SECONDS must be greater than zero.")

    raw_data_dir = PROJECT_ROOT / "data" / "raw"

    return {
        "api_url": api_url,
        "request_timeout_seconds": timeout,
        "raw_data_dir": raw_data_dir,
    }

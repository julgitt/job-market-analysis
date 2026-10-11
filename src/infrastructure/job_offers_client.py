import requests


class ApiClient:
    def __init__(self, api_url: str, timeout: int = 30):
        self.api_url = api_url
        self.timeout = timeout

    def fetch_job_offers(self) -> dict:
        try:
            response = requests.get(self.api_url, timeout=self.timeout)
            response.raise_for_status()
            payload = response.json()
        except requests.exceptions.RequestException as error:
            raise RuntimeError(f"Failed to fetch job offers: {error}") from error

        if not isinstance(payload, dict) or not isinstance(payload.get("data"), list):
            raise ValueError("The API response must contain a list in the 'data' field.")

        return payload

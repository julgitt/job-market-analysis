from src.config import load_settings
from src.infrastructure.job_offers_client import ApiClient
from src.infrastructure.json_job_offer_repository import JobOfferRepository


def fetch_job_offers() -> None:
    settings = load_settings()
    client = ApiClient(api_url=settings["api_url"], timeout=settings["request_timeout_seconds"])
    payload = client.fetch_job_offers()

    repository = JobOfferRepository(data_dir=settings["raw_data_dir"])
    output_path = repository.save_raw_data(payload)

    print(f"Job offers fetched and saved to: {output_path}")


if __name__ == "__main__":
    fetch_job_offers()

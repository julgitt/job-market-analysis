import json
from datetime import datetime
from pathlib import Path


class JobOfferRepository:
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir

    def save_raw_data(self, payload: dict) -> Path:
        self.data_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        file_path = self.data_dir / f"job_offers_{timestamp}.json"

        with file_path.open("w", encoding="utf-8") as file:
            json.dump(payload, file, ensure_ascii=False, indent=2)

        print(f"Raw job offer data saved to: {file_path}")

        return file_path

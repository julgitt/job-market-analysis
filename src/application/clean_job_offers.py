import json
import re
import html

from src.config import load_settings
from src.domain.job_offer_quality import validate_job_offer

def fix_slashes(text: str) -> str:
    if isinstance(text, str):
        return text.replace("\\/", "/").replace("\/", "/")
    return text

def clean_text(value: str) -> str:
    # unescape for double-encoded HTML
    value = html.unescape(html.unescape(value))
    # remove HTML tags
    value = re.sub(r"<[^>]+>", " ", value)
    # fix spaces
    value = value.replace("\xa0", " ")
    value = fix_slashes(value)
    # normalize whitespace
    value = re.sub(r"\s+", " ", value)

    return value.strip()


def get_latest_raw_file(raw_data_dir):
    raw_files = sorted(raw_data_dir.glob("job_offers_*.json"))
    return raw_files[-1] if raw_files else None


def load_json_payload(file_path):
    with file_path.open("r", encoding="utf-8") as file:
        payload = json.load(file)
    if not isinstance(payload, dict) or not isinstance(payload.get("data"), list):
        return None
    return payload


def process_single_offer(offer: dict, seen_slugs: set):
    if not isinstance(offer, dict):
        return None

    slug = offer.get("slug")
    company_name = offer.get("company_name")
    title = offer.get("title")

    if not all(isinstance(val, str) and val.strip() for val in (slug, company_name, title)):
        return None

    slug = slug.strip()
    if slug in seen_slugs:
        return None

    seen_slugs.add(slug)
    cleaned_offer = offer.copy()

    cleaned_offer["slug"] = slug
    cleaned_offer["company_name"] = fix_slashes(company_name.strip())
    cleaned_offer["title"] = fix_slashes(title.strip())

    description = cleaned_offer.get("description")
    if isinstance(description, str):
        cleaned_offer["description"] = clean_text(description)

    location = cleaned_offer.get("location")
    if isinstance(location, str):
        cleaned_offer["location"] = location.strip()

    for field in ["job_types", "tags"]:
        field_data = cleaned_offer.get(field)
        if isinstance(field_data, list):
            cleaned_offer[field] = [fix_slashes(item) for item in field_data]

    return cleaned_offer


def clean_job_offers() -> None:
    settings = load_settings()

    raw_data_dir = settings["raw_data_dir"]
    clean_data_dir = settings["clean_data_dir"]

    latest_file = get_latest_raw_file(raw_data_dir)
    if not latest_file:
        print("No raw job offer files found.")
        return

    payload = load_json_payload(latest_file)
    if not payload:
        print("Invalid raw data format: expected a JSON object with a 'data' list.")
        return

    offers = payload["data"]
    offers_with_quality_errors = 0
    quality_errors_count = 0
    cleaned_offers = []
    seen_slugs = set()

    for offer in offers:
        errors = validate_job_offer(offer)

        if errors:
            offers_with_quality_errors += 1
            quality_errors_count += len(errors)
            print(f"Quality issues in offer {offer.get('slug', '<unknown>')}:")
            for error in errors:
                print(f"  - {error}")

        processed_offer = process_single_offer(offer, seen_slugs)
        if processed_offer:
            cleaned_offers.append(processed_offer)

    clean_data_dir.mkdir(parents=True, exist_ok=True)
    output_path = clean_data_dir / "job_offers_clean.json"

    cleaned_payload = payload.copy()
    cleaned_payload["data"] = cleaned_offers

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(cleaned_payload, file, ensure_ascii=False, indent=2)

    print(f"Raw file: {latest_file}")
    print(f"Offers before cleaning: {len(offers)}")
    print(f"Offers after cleaning: {len(cleaned_offers)}")
    print(f"Clean data saved to: {output_path}")
    print(f"Offers with quality issues: {offers_with_quality_errors}")
    print(f"Total quality issues found: {quality_errors_count}")


if __name__ == "__main__":
    clean_job_offers()

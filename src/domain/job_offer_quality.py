def validate_job_offer(offer: dict) -> list[str]:

    errors = []

    for field in ("slug", "company_name", "title"):
        value = offer.get(field)

        if not isinstance(value, str) or not value.strip():
            errors.append(f"{field} must be a non-empty string")

    if not isinstance(offer.get("remote"), bool):
        errors.append("remote must be a boolean")

    url = offer.get("url")

    if not isinstance(url, str) or not url.startswith(("https://", "http://")):
        errors.append("url must start with http:// or https://")

    for field in ("tags", "job_types"):
        value = offer.get(field)

        if not isinstance(value, list):
            errors.append(f"{field} must be a list")
        elif not all(isinstance(item, str) for item in value):
            errors.append(f"{field} must contain only strings")

    created_at = offer.get("created_at")

    if not isinstance(created_at, int) or isinstance(created_at, bool):
        errors.append("created_at must be an integer")

    return errors


def find_duplicate_slugs(offers: list[dict]) -> list[str]:

    seen_slugs = set()
    duplicates = set()

    for offer in offers:
        slug = offer.get("slug")

        if not isinstance(slug, str) or not slug.strip():
            continue

        slug = slug.strip()

        if slug in seen_slugs:
            duplicates.add(slug)
        else:
            seen_slugs.add(slug)

    return sorted(duplicates)

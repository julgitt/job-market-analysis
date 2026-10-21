from src.application.clean_job_offers import clean_text
from src.domain.job_offer_quality import (
    validate_job_offer,
    find_duplicate_slugs,
)


def sample_offer() -> dict:
    return {
        "slug": "python-developer-berlin",
        "company_name": "Example Company",
        "title": "Python Developer",
        "description": "Develop software with Python.",
        "remote": True,
        "url": "https://example.com/jobs/python-developer",
        "tags": ["Engineering", "Python"],
        "job_types": ["Full-time"],
        "location": "Berlin",
        "created_at": 1792065313,
    }


# Text cleaning tests


def test_clean_text_removes_html_tags():
    assert clean_text("<p>Python Developer</p>") == "Python Developer"


def test_clean_text_decodes_html_entities():
    result = clean_text("Flexible working hours&amp;nbsp;available")

    assert "Flexible working hours" in result
    assert "available" in result
    assert "&amp;" not in result


def test_clean_text_removes_extra_whitespace():
    result = clean_text("  Python    Developer \n Berlin  ")

    assert result == "Python Developer Berlin"


def test_clean_text_handles_nested_html_entities():
    result = clean_text("&amp;lt;p&amp;gt;Data Analyst&amp;lt;/p&amp;gt;")

    assert result == "Data Analyst"


def test_clean_text_handles_empty_string():
    assert clean_text("") == ""


# Data quality tests


def test_valid_offer_has_no_errors():
    assert validate_job_offer(sample_offer()) == []


def test_missing_title_is_reported():
    offer = sample_offer()
    offer["title"] = "  "

    errors = validate_job_offer(offer)

    assert "title must be a non-empty string" in errors


def test_remote_must_be_boolean():
    offer = sample_offer()
    offer["remote"] = "true"

    errors = validate_job_offer(offer)

    assert "remote must be a boolean" in errors


def test_url_must_use_http_or_https():
    offer = sample_offer()
    offer["url"] = "example.com/job"

    errors = validate_job_offer(offer)

    assert "url must start with http:// or https://" in errors


def test_tags_must_contain_only_strings():
    offer = sample_offer()
    offer["tags"] = ["Python", 123]

    errors = validate_job_offer(offer)

    assert "tags must contain only strings" in errors


def test_created_at_must_be_an_integer():
    offer = sample_offer()
    offer["created_at"] = "1792065313"

    errors = validate_job_offer(offer)

    assert "created_at must be an integer" in errors


def test_duplicate_slugs_are_detected():
    offers = [
        sample_offer(),
        sample_offer(),
        {
            **sample_offer(),
            "slug": "data-analyst-berlin",
        },
    ]

    assert find_duplicate_slugs(offers) == ["python-developer-berlin"]

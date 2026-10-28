import json
import pandas as pd
from pathlib import Path

from src.config import load_settings


def save_as_json(df: pd.DataFrame, path: Path) -> None:
    df.to_json(path, orient="records", force_ascii=False, indent=4)


def build_gold_layer():
    settings = load_settings()
    clean_path = settings["clean_data_dir"] / "job_offers_clean.json"
    serving_dir = settings["serving_data_dir"]
    
    serving_dir.mkdir(parents=True, exist_ok=True)
    
    with open(clean_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    if isinstance(data, dict) and "data" in data:
        df = pd.DataFrame(data["data"])
    elif isinstance(data, list):
        df = pd.DataFrame(data)
    else:
        df = pd.DataFrame([data])

    display_columns = ['title', 'company_name', 'location', 'remote', 'job_types', 'tags']
    save_as_json(df[display_columns], serving_dir / "serving_job_offers.json")

    location_stats = df['location'].value_counts().reset_index()
    location_stats.columns = ['location', 'count']
    save_as_json(location_stats, serving_dir / "serving_location_stats.json")

    tags_exploded = df.explode('tags')
    tags_stats = tags_exploded['tags'].value_counts().reset_index()
    tags_stats.columns = ['tag', 'count']
    save_as_json(tags_stats, serving_dir / "serving_tags_summary.json")

    job_types_exploded = df.explode('job_types')
    job_types_stats = job_types_exploded['job_types'].value_counts().reset_index()
    job_types_stats.columns = ['job_type', 'count']
    save_as_json(job_types_stats, serving_dir / "serving_job_types_summary.json")

if __name__ == "__main__":
    build_gold_layer()
import json
import pandas as pd
from pathlib import Path

def build_gold_layer():
    base_dir = Path(__file__).resolve().parent.parent.parent
    clean_path = base_dir / "data" / "clean" / "job_offers_clean.json"
    serving_dir = base_dir / "data" / "serving"
    
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
    df_serving = df[display_columns].copy()
    df_serving.to_json(serving_dir / "serving_job_offers.json", orient="records", force_ascii=False, indent=4)

    location_stats = df['location'].value_counts().reset_index()
    location_stats.columns = ['location', 'count']
    location_stats.to_json(serving_dir / "serving_location_stats.json", orient="records", force_ascii=False, indent=4)

    tags_exploded = df.explode('tags')
    tags_stats = tags_exploded['tags'].value_counts().reset_index()
    tags_stats.columns = ['tag', 'count']
    tags_stats.to_json(serving_dir / "serving_tags_summary.json", orient="records", force_ascii=False, indent=4)

    job_types_exploded = df.explode('job_types')
    job_types_stats = job_types_exploded['job_types'].value_counts().reset_index()
    job_types_stats.columns = ['job_type', 'count']
    job_types_stats.to_json(serving_dir / "serving_job_types_summary.json", orient="records", force_ascii=False, indent=4)

if __name__ == "__main__":
    build_gold_layer()
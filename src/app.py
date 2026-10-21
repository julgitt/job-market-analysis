import streamlit as st
import pandas as pd
import json
from pathlib import Path

st.set_page_config(page_title="Analiza Rynku Pracy", layout="wide")

st.title("Dashboard: Analiza Ofert Pracy")
st.markdown("Ten dashboard prezentuje aktualne dane z rynku pracy na podstawie pobranych i oczyszczonych ofert.")

@st.cache_data
def load_data():
    base_dir = Path(__file__).resolve().parent.parent
    file_path = base_dir / "data" / "clean" / "job_offers_clean.json"
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        if "data" in data:
            df = pd.DataFrame(data["data"])
        else:
            df = pd.DataFrame(data)
            
        return df
    except Exception as e:
        st.error(f"Wystąpił błąd podczas ładowania danych: {e}")
        return pd.DataFrame()

df_raw = load_data()

if df_raw.empty:
    st.warning("Brak danych do wyświetlenia. Upewnij się, że plik JSON istnieje w data/clean/.")
    st.stop()

df_exploded = df_raw.explode('job_types').explode('tags')

st.sidebar.header("Filtry")

locations = df_raw['location'].dropna().unique().tolist()
selected_location = st.sidebar.multiselect("Wybierz lokalizację", options=locations, default=locations[:10])

job_types_list = df_exploded['job_types'].dropna().unique().tolist()
selected_job_types = st.sidebar.multiselect("Typ zatrudnienia / doświadczenie", options=job_types_list, default=job_types_list[:5])

df_filtered = df_raw[
    (df_raw['location'].isin(selected_location)) &
    (df_raw['job_types'].apply(lambda x: any(item in selected_job_types for item in x) if isinstance(x, list) else False))
]

st.subheader("Kluczowe wskaźniki")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Liczba ofert (odfiltrowane)", value=len(df_filtered))

with col2:
    st.metric(label="Liczba unikalnych firm", value=df_filtered['company_name'].nunique())

with col3:
    remote_count = len(df_filtered[df_filtered['remote'] == True])
    remote_pct = (remote_count / len(df_filtered) * 100) if len(df_filtered) > 0 else 0
    st.metric(label="Oferty w 100% zdalne", value=f"{remote_count} ({remote_pct:.1f}%)")

st.divider()

col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.subheader("Top 10 Lokalizacji")
    location_counts = df_filtered['location'].value_counts().head(10)
    st.bar_chart(location_counts)

with col_chart2:
    st.subheader("Najczęstsze typy umów/wymagania")
    job_types_counts = df_filtered.explode('job_types')['job_types'].value_counts().head(10)
    st.bar_chart(job_types_counts)

st.subheader("Popularne Tagi / Umiejętności")
tags_counts = df_filtered.explode('tags')['tags'].value_counts().head(15)
st.bar_chart(tags_counts)

st.subheader("Tabela ofert (odfiltrowane)")
display_columns = ['title', 'company_name', 'location', 'remote', 'job_types', 'tags']
st.dataframe(df_filtered[display_columns], use_container_width=True)
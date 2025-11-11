import streamlit as st
import pandas as pd
from pathlib import Path
st.set_page_config(page_title="HyperStream HIL Console", layout="wide")
st.title("HyperStream – Human-in-the-Loop Console")

alerts_path = Path("data/sample_parquet/alerts.parquet")
raw_path = Path("data/sample_parquet/raw.parquet")

def ensure_alerts():
    if alerts_path.exists():
        return
    if not raw_path.exists():
        st.warning("No raw data found. Generating sample data...")
        import numpy as np
        rng = np.random.default_rng(7)
        rows=[]
        for i in range(1000):
            ts = i*10
            for c in range(6):
                val = np.sin(i/30 + c) + rng.normal(0,0.1)
                rows.append((f"ch_{c:03d}", ts, val))
        raw = pd.DataFrame(rows, columns=["sensor_id","ts","value"])
        raw_path.parent.mkdir(parents=True, exist_ok=True)
        raw.to_parquet(raw_path, index=False)
    raw = pd.read_parquet(raw_path)
    z = (raw["value"] - raw["value"].mean())/(raw["value"].std()+1e-6)
    raw = raw.assign(_z=z.abs())
    last = raw.sort_values("ts").groupby("sensor_id").tail(1).copy()
    alerts = last[["sensor_id","ts","_z"]].rename(columns={"_z":"severity"})
    alerts["severity"] = alerts["severity"].clip(0,5)
    alerts["label"] = None
    alerts.to_parquet(alerts_path, index=False)

colA, colB = st.columns([1,3])
with colA:
    if st.button("Generate sample alerts", use_container_width=True):
        ensure_alerts()
        st.success("Alerts generated.")
with colB:
    st.caption("If empty, click the button to generate demo alerts.")

if alerts_path.exists():
    df = pd.read_parquet(alerts_path)
    st.dataframe(df, use_container_width=True, height=420)
else:
    st.info("No alerts yet. Click **Generate sample alerts**.")

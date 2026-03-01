import streamlit as st
import os
from pathlib import Path
import pandas as pd 
import matplotlib.pyplot as plt
# use this so it does not lose context
HERE = Path(__file__).resolve().parent
img_path = HERE / "static" / "qualityxdark.png"   # or qualityx.jpg
img_path_1 = HERE / "static" / "qualityx.png"   # or qualityx.jpg


st.title("Qualityx AI" )
st.image(str(img_path), caption="Call center analytics in action")


st.header("Analytics for call centers of the future")
st.subheader("What's a call center without analytics? ")
st.markdown(" This is the AI _future_ of call centers, and we're here to help you *get there*. ")

st.subheader("Data Frame Edge AI comparison")

df_edge_devices = pd.DataFrame([
    {
        "Approach": "Manual QA",
        "Calls reviewed per day": 15,
        "Review coverage": "Sample",
        "Latency": "Human-time (hours/days)",
        "Consistency": "Variable",
        "Cost profile": "High labor / linear scaling",
        "Privacy/Edge": "Often cloud tools; depends on process",
        "Best for": "Deep audits, coaching, edge cases",
    },
    {
        "Approach": "AI QA (Cloud)",
        "Calls reviewed per day": 100,
        "Review coverage": "High (near-continuous)",
        "Latency": "Minutes",
        "Ram": "N/A (cloud resources)",
        "Disk_GB": "N/A (cloud resources)",
        "Disk_Type": "N/A (cloud resources)",
        "Disk_Read": "N/A (cloud resources)",
        "Consistency": "High (policy-driven)",
        "Cost profile": "Medium / usage-based",
        "Privacy/Edge": "Lower (audio leaves premises)",
        "Best for": "Scale, dashboards, trends",
    },
    {
        "Approach": "AI QA (Edge: Orange Pi 5 Pro 4 gb)",
        "Calls reviewed per day": 60,
        "Review coverage": "Medium-high",
        "Latency": "Near real-time",
        "Ram": "4GB",
        "Disk_GB": 64,
        "Disk_Type": "eMMC",
        "Disk_Read": "400mb/s",
        "Consistency": "High (policy-driven)",
        "Cost profile": "Low ongoing / hardware + power",
        "Privacy/Edge": "Highest (on-device processing)",
        "Best for": "Privacy-first sites, offline/limited bandwidth",
    },
    {
        "Approach": "AI QA (Edge: Orange Pi Plus 5)",
        "Calls reviewed per day": 120,
        "Review coverage": "High",
        "Latency": "Real-time",
        "Ram": "8GB",
        "Disk_GB": 128,
        "Disk_Type": "eMMC",
        "Disk_Read": "400mb/s",
        "Consistency": "High (policy-driven)",
        "Cost profile": "Low ongoing / hardware + power",
        "Privacy/Edge": "Highest (on-device processing)",
        "Best for": "High throughput edge + privacy",
    },
    {
        "Approach": "AI QA (Edge: Raspberry Pi 5)",
        "Calls reviewed per day": 40,
        "Review coverage": "Medium",
        "Latency": "Near real-time",
        "Ram": "8GB",
        "Disk_GB": 800,
        "Disk_Type": "SSD",
        "Disk_Read": "800mb/s",
        "Consistency": "High (policy-driven)",
        "Cost profile": "Low ongoing / hardware + power",
        "Privacy/Edge": "Highest (on-device processing)",
        "Best for": "Lightweight models, basic scoring",
    }
])
st.dataframe(df_edge_devices)

# creating metrics 
st.metric(label="Manual QA", value="15 calls/day", delta="N/A")
st.metric(label="AI QA (Cloud)", value="100 calls/day", delta="+85 calls/day")  
# call reivewed per day but where approach is ai
st.metric(label="Ai avg:", value=round(df_edge_devices[df_edge_devices["Approach"].str.contains("AI")]["Calls reviewed per day"].mean(), 2), delta="+85 calls/day")


# Charts here 
# Filter only rows with numeric Disk_GB for the charts
df_chart = df_edge_devices[
    df_edge_devices["Disk_GB"].apply(lambda x: isinstance(x, (int, float))) # filter only columns that have int or float values in Disk_GB
].copy()

df_chart = df_chart[["Approach", "Disk_GB", "Calls reviewed per day"]].set_index("Approach")
st.subheader('area chart')
st.area_chart(df_chart)

st.subheader('scatter chart')
st.scatter_chart(df_chart)

st.subheader('bar chart')
st.bar_chart(df_chart)

st.subheader('line chart')
st.line_chart(df_chart)


Latitude: 4.7110
Longitude: -74.0721

st.subheader("Call center locations")
st.map(pd.DataFrame({
    "lat": [4.7110, 12.8797, 34.0522],
    "lon": [-74.0721, 121.7740, -118.2437],
    "Location": ["Bogotá", "Philippines", "California"]
}))

st.subheader("Brands Dictionary")
brands_dict = {
    "Orange PI": "https://www.orangepi.org/",
    "Raspberry Pi": "https://www.raspberrypi.com/",
    "Azure": "https://azure.microsoft.com/en-us/services/ai/",
    "AWS": "https://aws.amazon.com/machine-learning/",
}
st.json(brands_dict)

st.caption("Don't worry this is not AGI yet")
code = """
def greet(name):
    print(f"Hello, {name}!")
"""
st.code(code, language="python")
st.divider()



st.image(str(img_path_1), caption="Call center analytics in action")

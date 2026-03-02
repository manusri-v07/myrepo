#!/usr/bin/env python3

"""
SIMPLE REFLEX AGENT — AQI MONITOR
CPCB India Method
"""

import pandas as pd
import numpy as np
import os


# ─────────────────────────────────────────────────────────
# SUB-INDEX FUNCTIONS (CPCB Breakpoints)
# ─────────────────────────────────────────────────────────

def get_PM25_subindex(x):
    if pd.isna(x) or x < 0:
        return 0
    if x <= 30:   return x * 50 / 30
    elif x <= 60: return 50 + (x - 30) * 50 / 30
    elif x <= 90: return 100 + (x - 60) * 100 / 30
    elif x <= 120: return 200 + (x - 90) * 100 / 30
    elif x <= 250: return 300 + (x - 120) * 100 / 130
    else: return 400 + (x - 250) * 100 / 130


def get_PM10_subindex(x):
    if pd.isna(x) or x < 0:
        return 0
    if x <= 50: return x
    elif x <= 100: return x
    elif x <= 250: return 100 + (x - 100) * 100 / 150
    elif x <= 350: return 200 + (x - 250)
    elif x <= 430: return 300 + (x - 350) * 100 / 80
    else: return 400 + (x - 430) * 100 / 80


def get_NOx_subindex(x):
    if pd.isna(x) or x < 0:
        return 0
    if x <= 40: return x * 50 / 40
    elif x <= 80: return 50 + (x - 40) * 50 / 40
    elif x <= 180: return 100 + (x - 80) * 100 / 100
    elif x <= 280: return 200 + (x - 180) * 100 / 100
    elif x <= 400: return 300 + (x - 280) * 100 / 120
    else: return 400 + (x - 400) * 100 / 120


def get_SO2_subindex(x):
    if pd.isna(x) or x < 0:
        return 0
    if x <= 40: return x * 50 / 40
    elif x <= 80: return 50 + (x - 40) * 50 / 40
    elif x <= 380: return 100 + (x - 80) * 100 / 300
    elif x <= 800: return 200 + (x - 380) * 100 / 420
    elif x <= 1600: return 300 + (x - 800) * 100 / 800
    else: return 400 + (x - 1600) * 100 / 800


def get_CO_subindex(x):
    if pd.isna(x) or x < 0:
        return 0
    if x <= 1: return x * 50
    elif x <= 2: return 50 + (x - 1) * 50
    elif x <= 10: return 100 + (x - 2) * 100 / 8
    elif x <= 17: return 200 + (x - 10) * 100 / 7
    elif x <= 34: return 300 + (x - 17) * 100 / 17
    else: return 400 + (x - 34) * 100 / 17


# ─────────────────────────────────────────────────────────
# AQI CATEGORY RULES (Simple Reflex Rules)
# ─────────────────────────────────────────────────────────

def get_category(aqi):
    if pd.isna(aqi):
        return "UNKNOWN", "Insufficient data."

    aqi = round(aqi)

    if aqi <= 50:
        return "GOOD", "Air quality is satisfactory."
    elif aqi <= 100:
        return "SATISFACTORY", "Minor discomfort to sensitive people."
    elif aqi <= 200:
        return "MODERATE", "Discomfort for people with lung/heart disease."
    elif aqi <= 300:
        return "POOR", "Breathing discomfort on prolonged exposure."
    elif aqi <= 400:
        return "VERY POOR", "Respiratory illness on prolonged exposure."
    else:
        return "SEVERE", "Health emergency. Stay indoors."


# ─────────────────────────────────────────────────────────
# AGENT FUNCTION (Percept → Action)
# ─────────────────────────────────────────────────────────

def compute_aqi(row):

    sub_indices = {
        "PM2.5": get_PM25_subindex(row.get("PM2.5", np.nan)),
        "PM10":  get_PM10_subindex(row.get("PM10", np.nan)),
        "NOx":   get_NOx_subindex(row.get("NOx", np.nan)),
        "SO2":   get_SO2_subindex(row.get("SO2", np.nan)),
        "CO":    get_CO_subindex(row.get("CO", np.nan)),
    }

    valid_count = sum(1 for v in sub_indices.values() if v > 0)
    pm_available = (sub_indices["PM2.5"] > 0) or (sub_indices["PM10"] > 0)

    if not pm_available or valid_count < 3:
        return np.nan, sub_indices

    final_aqi = max(sub_indices.values())
    return final_aqi, sub_indices


# ─────────────────────────────────────────────────────────
# MAIN AGENT LOOP
# ─────────────────────────────────────────────────────────

def run_agent(csv_path):

    if not os.path.exists(csv_path):
        print(f"[INFO] '{csv_path}' not found. Running demo mode.\n")
        run_demo()
        return

    df = pd.read_csv(csv_path)

    print("=" * 60)
    print("AQI MONITOR — Simple Reflex Agent")
    print("=" * 60)

    for idx, row in df.iterrows():
        aqi, sub = compute_aqi(row)
        category, advisory = get_category(aqi)

        timestamp = row.get("Datetime", f"Row {idx+1}")

        print(f"\nTimestamp : {timestamp}")
        print(f"AQI       : {round(aqi) if not pd.isna(aqi) else 'N/A'}")
        print(f"Category  : {category}")
        print(f"Advisory  : {advisory}")

        dominant = max(sub, key=sub.get)
        print(f"Dominant  : {dominant} ({sub[dominant]:.1f})")

        print("-" * 60)


# ─────────────────────────────────────────────────────────
# DEMO MODE
# ─────────────────────────────────────────────────────────

def run_demo():

    demo_data = [
        {"Datetime": "Example 1", "PM2.5": 200, "PM10": 225, "NOx": 55, "SO2": 30, "CO": 2.0},
        {"Datetime": "Example 2", "PM2.5": 1200, "PM10": 1400, "NOx": 80, "SO2": 45, "CO": 5.0},
        {"Datetime": "Example 3", "PM2.5": 20, "PM10": 35, "NOx": 20, "SO2": 15, "CO": 0.5},
    ]

    print("=" * 60)
    print("AQI DEMO MODE")
    print("=" * 60)

    for row in demo_data:
        aqi, sub = compute_aqi(row)
        category, advisory = get_category(aqi)

        print(f"\nTimestamp : {row['Datetime']}")
        print(f"AQI       : {round(aqi)}")
        print(f"Category  : {category}")
        print(f"Advisory  : {advisory}")
        print("-" * 60)


# ─────────────────────────────────────────────────────────

if __name__ == "__main__":
    run_agent("sensor_data.csv")

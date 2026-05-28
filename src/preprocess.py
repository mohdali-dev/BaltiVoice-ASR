"""
BaltiVoice ASR — Data Audit & Preprocessing
Run this script to audit your dataset and create train/dev splits.
"""

import os
import json
import numpy as np
import pandas as pd
import librosa
from tqdm import tqdm
from sklearn.model_selection import train_test_split

# ── CONFIG ───────────────────────────────────────────────────
CLIPS_BASE  = "./data/wavs"
TRAIN_LIST  = "./data/train_list.txt"
OUTPUT_DIR  = "./data/processed"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_dataset(train_list_path: str) -> pd.DataFrame:
    """Load train_list.txt into a DataFrame."""
    rows = []
    with open(train_list_path) as f:
        for line in f:
            line = line.strip()
            if "|" not in line:
                continue
            path, sentence = line.split("|", 1)
            rows.append({"path": path.strip(), "sentence": sentence.strip()})

    df = pd.DataFrame(rows)
    df["full_path"]  = df["path"].apply(lambda p: os.path.join(CLIPS_BASE, os.path.basename(p)))
    df["word_count"] = df["sentence"].str.split().str.len()
    df["char_len"]   = df["sentence"].str.len()
    return df


def verify_audio(df: pd.DataFrame) -> pd.DataFrame:
    """Check all audio files exist on disk."""
    missing = []
    for _, row in tqdm(df.iterrows(), total=len(df), desc="Verifying audio"):
        if not os.path.exists(row["full_path"]):
            missing.append(row["path"])

    print(f"✅ Found  : {len(df) - len(missing):,}")
    print(f"❌ Missing : {len(missing):,}")

    return df[~df["path"].isin(missing)].reset_index(drop=True)


def estimate_duration(df: pd.DataFrame, sample_n: int = 500) -> float:
    """Estimate total dataset hours from a sample."""
    sample    = df.sample(min(sample_n, len(df)), random_state=42)
    durations = []

    for _, row in tqdm(sample.iterrows(), total=len(sample), desc="Measuring durations"):
        try:
            durations.append(librosa.get_duration(path=row["full_path"]))
        except Exception:
            pass

    mean_dur  = np.mean(durations)
    est_hours = (mean_dur * len(df)) / 3600
    print(f"Mean duration : {mean_dur:.2f}s")
    print(f"Total audio   : ~{est_hours:.1f} hours")
    return est_hours


def create_splits(df: pd.DataFrame, test_size: float = 0.10) -> tuple:
    """Clean and split into train/dev."""
    df_clean = df[df["word_count"] >= 2].reset_index(drop=True)
    train_df, dev_df = train_test_split(df_clean, test_size=test_size, random_state=42)

    train_df.to_csv(f"{OUTPUT_DIR}/train.tsv", sep="\t", index=False)
    dev_df.to_csv(f"{OUTPUT_DIR}/dev.tsv",     sep="\t", index=False)

    print(f"Train : {len(train_df):,}")
    print(f"Dev   : {len(dev_df):,}")
    return train_df, dev_df


if __name__ == "__main__":
    print("Loading dataset...")
    df = load_dataset(TRAIN_LIST)
    print(f"Total samples: {len(df):,}")

    print("\nVerifying audio files...")
    df = verify_audio(df)

    print("\nEstimating duration...")
    est_hours = estimate_duration(df)

    print("\nCreating splits...")
    train_df, dev_df = create_splits(df)

    report = {
        "total_samples" : len(df),
        "train_size"    : len(train_df),
        "dev_size"      : len(dev_df),
        "est_hours"     : round(est_hours, 2),
    }

    with open(f"{OUTPUT_DIR}/audit_report.json", "w") as f:
        json.dump(report, f, indent=2)

    print(f"\n✅ Done — {json.dumps(report, indent=2)}")

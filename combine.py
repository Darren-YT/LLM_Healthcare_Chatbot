# combine.py — no-arg
import pandas as pd, re
from pathlib import Path

IN  = Path("emotion-emotion_69k.csv")
OUT = Path("emotion-emotion_69k.cleaned.csv")

df = pd.read_csv(IN).fillna("")
col = "empathetic_dialogues"
assert col in df.columns, f"can not find column {col}"

df[col] = (
    df[col].astype(str)
      .str.replace(r"\r\n?","\n", regex=True)
      .str.replace(r"(?m)^\s*(?:Customer|Agent)\s*:\s*", "", regex=True)
      .str.replace(r"[ \t]+\n","\n", regex=True)
      .str.replace(r"\s{2,}", " ", regex=True)
      .str.strip()
)

df.to_csv(OUT, index=False)
print(f"Saved → {OUT}")

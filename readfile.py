import pandas as pd
df = pd.read_json("combined_chatbot_dataset.jsonl", lines=True)
print(df)
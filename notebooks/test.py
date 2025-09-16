import pandas as pd

data = {"Name": ["Harrison", "Grant"], "Score": [95, 88]}
df = pd.DataFrame(data)
df["Passed"] = df["Score"] >= 90
print(df)


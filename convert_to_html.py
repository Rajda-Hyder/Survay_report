import pandas as pd

df = pd.read_csv("student_data.csv")
df.to_html("index.html", index=False)

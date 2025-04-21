import pandas as pd

# -------------------------
# Made by: Syeda Rajda Bano
# Roll No: 00162420
# Class: GIAIC
# Day & Slot: Wednesday 7pm-10pm
# -------------------------

df = pd.read_csv("student_data.csv")
df.to_html("index.html", index=False)

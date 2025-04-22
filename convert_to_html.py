import pandas as pd
from datetime import datetime

# Read CSV file
df = pd.read_csv("student_data.csv")

# Generate HTML table 
table_html = df.to_html(index=False)

# Current date update
current_date = datetime.now().strftime("%d %B %Y")

# Generate Full HTML page 
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Survey Report</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            text-align: center;
        }}
        table {{
            width: 80%;
            margin: 20px auto;
            border-collapse: collapse;
            background-color: #fff;
        }}
        th, td {{
            padding: 10px;
            border: 1px solid #ddd;
        }}
    </style>
</head>
<body>
    <h2>Survey Report</h2>
    <h4>
        Made by: <strong>Syeda Rajda Bano</strong> | Roll No: <strong>00162420</strong> <br>
        Class: <strong>GIAIC</strong> | Day & Slot: <strong>Wednesday 7pm–10pm</strong><br>
        <span style='color: gray;'>Last Updated: {current_date}</span>
    </h4>
    <hr>
    {table_html}
</body>
</html>
"""

# HTML file save karo
with open("index.html", "w", encoding="utf-8") as file:
    file.write(html_content)

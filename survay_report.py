# imports
import csv

with open('student_data.csv', newline = "") as file:
    reader = csv.DictReader(file)

    print("\n📋 STUDENT SURVEY REPORT 📋")
    print("="*45)

    for row in reader:
        print(f"Name       : {row['Name']}")
        print(f"Roll No    : {row['Roll No']}")
        print(f"Contact No : {row['Contact No']}")
        print(f"Progress   : {row['Progress']}")
        print("-"*45)

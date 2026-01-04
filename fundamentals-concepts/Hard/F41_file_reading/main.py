

from pathlib import Path
import json
import csv

Base = Path(__file__).resolve().parent

file_path = Base / "input.txt"
file_path1 = Base / "input.json"
file_path2 = Base / "input.csv"

try:
    with open(file_path, 'r') as file:
        
        content = file.readline()
        print(content)

    with open(file_path1, 'r') as file:
        content_json = json.load(file)
        for line in content_json["students"]:
            print(f"{line["id"]} | {line["name"]:10} | {line["age"]} | {line["course"]:10} | {line["cgpa"]}")
    
    print("CSV data:")
    with open(file_path2, 'r') as file:
        content_csv = csv.reader(file)
        for line in content_csv:
            print(f"{line[0]:5} | {line[1]:15} | {line[2]:5} | {line[3]:25} | {line[4]}")
except FileNotFoundError:
    print("This file is not found")
except PermissionError:
    print("This file has no access to you")
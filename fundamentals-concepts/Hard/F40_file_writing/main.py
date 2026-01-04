'''
file Writing methods:
'w': it writes into existing file. It override the existing file if there 
'x': It creates a new file and write data into it. If file already exist, it throws an error
'a': It append records to the last
'r': It read the file
'
'''

from pathlib import Path

import json
import csv

student = {"name":"afnan", "age": 25, "school":"BBHS"}

table = [["Name", "roll no", "class"],
         ["Afnan", 25, 5],
         ["Sam", 27, 8]]
text_data = "I like a chocos"
BASE = Path(__file__).resolve().parent

employees = ["afnan", "nikhil", "moiz"]

file_path = BASE / "Output.txt"
file_path1 = BASE / "Output1.txt"
file_path2 = BASE / "my_output.json"
file_path3 = BASE / "my_output.csv"
#with automatically close the file after use
# as keyword set the filename to 'file'
try:
    with open(file_path, 'a') as file: 
        #file.write(text_data)
        file.write('\n' + text_data) # this adds new line while appending (mode) data

    #we can write only string data into a file. others throw error, so for list, we have to traverse like below
    with open(file = file_path1, mode = 'w') as file:
        for i in employees:
            file.write(i + '\n')
    
    #Below we create a json file from the dictionary
    with open(file_path2, mode = 'w') as file:
        json.dump(student, file, indent=5) # This create a josn data with '5' indentation

    #Below we create a CSV file 
    with open(file_path3, 'w') as file:
        writer = csv.writer(file)
        for row in table:
            writer.writerow(row)
            
except FileExistsError:
    print("This file already exists")
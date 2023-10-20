import csv
import json



def csv_to_json(csv_filepath, json_filepath):
    """Convert a CSV file to JSON format."""
    with open(csv_filepath, 'r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        data = [row for row in csv_reader]
        
    with open(json_filepath, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Usage
csv_filepath = "/Users/troyperment/Development/DataFiles/input/csv_table.csv"
json_filepath = "/Users/troyperment/Development/DataFiles/output/json_table.json"
csv_to_json(csv_filepath, json_filepath)
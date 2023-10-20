# This script converts a CSV file to a JSON file. It is called by /Users/troyperment/Development/first-try/CalendarCreation/CalendarCreate.py
import csv
import json
import sys


# Define a function to read a CSV and convert to JSON.
def csvjson(csv_filepath, json_filepath):
    # Create an empty list to store the rows
    data = []

    # Read the CSV
    with open(csv_filepath, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        # Convert each row into a dictionary and add to data
        for row in csv_reader:
            # Convert the comma-separated days_of_week string to a list
            row['days_of_week'] = row['days_of_week'].split(", ")
            data.append(row)

    # Write the data to a JSON file
    with open(json_filepath, 'w') as json_file:
        json.dump(data, json_file, indent=4)






# Use the function
csv_filepath = r'/Users/troyperment/Development/DataFiles/input/schedules.csv'
json_filepath = r'/Users/troyperment/Development/DataFiles/output/schedules.json'
csvjson(csv_filepath, json_filepath)


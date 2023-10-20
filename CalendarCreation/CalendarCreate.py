
import json
from icalendar import Event, Calendar
from datetime import datetime
import subprocess



#with open("/Users/troyperment/Development/first-try/CalendarCreation/csv-json.py") as f:
#    exec(f.read())



#csvFilePath = r'/Users/troyperment/Development/DataFiles/input/schedules.csv'
#jsonFilePath = r'/Users/troyperment/Development/DataFiles/output/schedules.json'
#csv_to_json(csvFilePath, jsonFilePath)

# Load schedules from the JSON file
with open('/Users/troyperment/Development/DataFiles/output/schedules.json', 'r') as file:
    schedules = json.load(file)

# Verify if the loaded data is a list; if not, raise an error
if not isinstance(schedules, list):
    raise ValueError("Expected a list of schedules in the JSON file!")

# Convert schedules to iCalendar events
for schedule in schedules:
    # Ensure each schedule is a dictionary; if not, skip to the next schedule
    if not isinstance(schedule, dict):
        continue

    # Create a new calendar for each schedule
    cal = Calendar()

    event = Event()
    event.add('summary', schedule['name'])

    # Assuming start date is today. Adjust if needed.
    start_time = datetime.combine(datetime.today(), datetime.strptime(schedule['start_time'], "%H:%M").time())
    end_time = datetime.combine(datetime.today(), datetime.strptime(schedule['end_time'], "%H:%M").time())

    event.add('dtstart', start_time)
    event.add('dtend', end_time)

    # Add recurrence rule if the event is repeating
    if schedule['freq'] == 'Daily':
        event.add('rrule', {'freq': 'daily'})
    elif 'Weekly' in schedule['freq']:
        days = [day.upper()[:2] for day in schedule['days_of_week']]
        
        event.add('rrule', {'freq': 'weekly', 'byday': days})
        print(days)
    elif 'Monthly' in schedule['freq']:
        days = [day.upper()[:2] for day in schedule['days_of_week']]
        event.add('rrule', {'freq': 'monthly', 'byday': days})

    # Add the event to the calendar
    print(event)
    cal.add_component(event)

    # Save to a unique .ics file based on the event name
    filename = '/Users/troyperment/Development/DataFiles/output/' +schedule['name'].replace(' ', '_') + ".ics"
    with open(filename, "wb") as f:
        f.write(cal.to_ical())
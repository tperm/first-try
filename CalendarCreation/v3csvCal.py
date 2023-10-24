import csv
from icalendar import Event, Calendar, Alarm
from datetime import datetime, timedelta


# Load schedules from the CSV input
schedules = []
with open('/Users/troyperment/Development/DataFiles/input/schedules.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        schedules.append(row)

# Convert schedules to iCalendar events
for schedule in schedules:
    # Create a new calendar for each schedule
    cal = Calendar()

    event = Event()
    event.add('summary', schedule['summary'])
    event.add('description', row['description'])

    # Assuming start date is today. Adjust if needed.
    start_time = datetime.combine(datetime.today(), datetime.strptime(schedule['start_time'], "%H:%M").time())
    end_time = datetime.combine(datetime.today(), datetime.strptime(schedule['end_time'], "%H:%M").time())

    event.add('dtstart', start_time)
    event.add('dtend', end_time)
    alarm = Alarm()
    alarm.add('action', 'DISPLAY')
    alarm.add('description', 'Reminder for the important meeting')
    alarm.add('trigger', timedelta(minutes=-15))
    event.add_component(alarm)

    # Add recurrence rule if the event is repeating
    freq = schedule['freq'].upper()
    if freq == 'DAILY':
        event.add('rrule', {'freq': 'daily'})
    elif freq == 'WEEKLY':
        days = [day.upper() for day in schedule['days_of_week'].split(',')]
        event.add('rrule', {'freq': 'weekly', 'byday': days})
    elif freq == 'MONTHLY':
        event.add('rrule', {'freq': 'monthly'})
    elif freq == 'QUARTERLY':
        event.add('rrule', {'freq': 'monthly', 'interval': 3})

    # Add the event to the calendar
    cal.add_component(event)

    # Save to a unique .ics file based on the event name
    filename = '/Users/troyperment/Development/DataFiles/output/' +schedule['summary'].replace(' ', '_') + ".ics"
    with open(filename, "wb") as f:
        f.write(cal.to_ical())

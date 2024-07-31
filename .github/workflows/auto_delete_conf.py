import ruamel.yaml
from datetime import datetime

# Load the YAML file
yaml = ruamel.yaml.YAML()
with open('_data/conferences.yml', 'r') as file:
    conferences = yaml.load(file)

# Get the current month and year
today = datetime.now()
current_month = today.month
current_year = today.year

# Function to parse the month from a date string
def get_month(date_str):
    try:
        # Extract the first word and convert it to a month number
        month_str = date_str.split(' ')[0]
        return datetime.strptime(month_str, '%B').month
    except ValueError:
        return None

# Lists to track filtered and deleted conferences
filtered_conferences = []
deleted_conferences = []  # Store names of conferences that are removed

for conf in conferences:
    conf_date = conf.get('date', '--')
    if conf_date != "--":
        conf_month = get_month(conf_date)
        if conf_month:
            # Calculate the next month considering year rollover
            next_month = (conf_month % 12) + 1
            # Use the same year unless it rolls over to January
            next_month_year = current_year if conf_month < 12 else current_year + 1

            # Determine if the conference is in the past
            if (current_year > next_month_year) or (current_year == next_month_year and current_month > next_month):
                deleted_conferences.append(conf['title'])  # Log the deleted conference
                continue  # Skip adding this conference to the list

    # Add the conference if it hasn't been skipped
    filtered_conferences.append(conf)

# Write the filtered list back to the YAML file
with open('_data/conferences_filtered.yml', 'w') as file:
    yaml.dump(filtered_conferences, file)

# Print the titles of conferences that were deleted
print("Deleted conferences:")
for title in deleted_conferences:
    print(title)

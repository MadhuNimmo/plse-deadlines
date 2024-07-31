import yaml
import datetime
from ruamel.yaml import YAML

# Load YAML file
yaml = YAML()
with open('_data/conferences.yml', 'r') as file:
    conferences = yaml.load(file)

# Filter out past conferences
conferences['conferences'] = [
    conf for conf in conferences['conferences']
    if datetime.datetime.strptime(conf['date'], '%Y-%m-%d') > datetime.datetime.now()
]

# Write back to YAML file
with open('_data/conferences.yml', 'w') as file:
    yaml.dump(conferences, file)

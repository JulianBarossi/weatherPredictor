# loading and inspecting the contents of JSON file 
import json

# Load the JSON file
file_path = '/mnt/data/climate.json'

with open(file_path, 'r') as file:
    climate_data = json.load(file)

# Display the first few entries to understand the structure of the data
climate_data[:5]

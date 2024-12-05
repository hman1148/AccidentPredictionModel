import pandas as pd
import os

# File path for Linux
file_path = 'custom_file_path'

# Load specific sheets from the Excel file
crash_data = pd.read_excel(file_path, sheet_name='Crash data 2019-2021')
vehicle_data = pd.read_excel(file_path, sheet_name='Vehicle data 2019-2021')

# Merge the data on 'crash_id' with an outer join
merged_data = pd.merge(crash_data, vehicle_data, on='crash_id', how='outer')

# Define the required columns
required_columns = [
    'crash_severity_id_x',
    'vehicle_maneuver_id',
    'vehicle_contrib_circum_id',
    'extent_deformity_id',
    'most_damaged_area_id',
    'area_init_impact_id',
    'most_harmful_event_id',
    'event_sequence_1_id',
    'event_sequence_2_id',
    'event_sequence_3_id',
    'event_sequence_4_id',
    'crash_severity_id_y',
    'crash_datetime_y',
    'first_harmful_event_id',
    'roadway_contrib_circum_id',
    'lat',
    'long'
]

# Filter merged data to include only the required columns
filtered_data = merged_data[required_columns]

output_file = os.path.expanduser('data_location')
os.makedirs(os.path.dirname(output_file), exist_ok=True)

filtered_data.to_csv(output_file, index=False)

print(f"Filtered data saved to {output_file}")

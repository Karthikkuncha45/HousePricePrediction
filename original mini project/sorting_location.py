import pandas as pd
file_path = r'C:\\Users\\kunch\\OneDrive\\Documents\\Desktop\\original mini project\\Mumbai.csv'

try:
    # Read the CSV file
    data = pd.read_csv(file_path)

    # Extract the 'location' column
    if 'Location' in data.columns:
        locations = data['Location'].dropna().unique()  # Remove NaN values and get unique locations
        sorted_locations = sorted(locations)  # Sort locations alphabetically
        print(sorted_locations) # Display the first 10 sorted locations as a preview
    else:
        "The dataset does not contain a 'location' column."
except Exception as e:
    str(e)
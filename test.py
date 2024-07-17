#!/usr/bin/env python3

import pandas as pd
from datetime import datetime

# Define the file path
dest_dir = "/Users/karinabao/github-projects/ritter-ipo-analysis/"
today = datetime.today().strftime('%Y%m%d')
file_path = "ipo-analysis.xlsx"

# Load the Excel file
ipo_data = pd.read_excel(file_path)

# Display the first few rows of the data
# print("First few rows of the dataset:")
# print(ipo_data.head())

# print("Size of data set")
# print(f"Rows: {ipo_data.shape[0]}")


# Basic analysis examples
# print("\nBasic Statistics:")
# print(ipo_data.describe())

# print("\nColumn Names:")
# print(ipo_data.columns)

# Example: Group by Year and calculate the mean age
# if 'Year' in ipo_data.columns and 'Age' in ipo_data.columns:
#     mean_age_by_year = ipo_data.groupby('Year')['Age'].mean()
#     print("\nMean Age by Year:")
#     print(mean_age_by_year)

# # Save the analysis results to a new Excel file
# analysis_file_path = f"{dest_dir}{today}-IPO-analysis-results.xlsx"
# with pd.ExcelWriter(analysis_file_path, engine='openpyxl') as writer:
#     ipo_data.describe().to_excel(writer, sheet_name='Basic Statistics')
#     if 'Year' in ipo_data.columns and 'Age' in ipo_data.columns:
#         mean_age_by_year.to_excel(writer, sheet_name='Mean Age by Year')

# print(f"\nAnalysis results saved to {analysis_file_path}")


# Convert the offering_date column to datetime
# ipo_data['offer date'] = pd.to_datetime(ipo_data['offer date'], errors='coerce')

# Filter the data for IPOs in 2023
# ipos_2023 = ipo_data[(ipo_data['offer date'] >= 20230000) & ((ipo_data['VC'] == "1") | (ipo_data['VC'] == "2" ))]
ipos_2023 = ipo_data.loc[(ipo_data['offer date'] >= 20100000)  & (ipo_data['VC'] == 1)]

# Display the filtered data
ipos_2023_list = ipos_2023[['IPO name', 'ticker', 'offer date', 'VC']]
print("List of IPOs in 2023:")
print(ipos_2023_list)


# ipos_2023 = ipo_data.loc[(ipo_data['offer date'] >= 20230000)  & (ipo_data['VC'] == 0)]
# ipos_2023_list = ipos_2023[['IPO name', 'ticker', 'offer date', 'VC', "Post-issue shares"]]
# print("List of IPOs in 2023:")
# print(ipos_2023_list.to_string())



# vc_unique_values = ipo_data['VC'].unique()
# print("Unique values in the 'VC' column:")
# print(vc_unique_values)

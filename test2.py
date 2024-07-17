#!/usr/bin/env python3

import pandas as pd
from datetime import datetime

# Define the file path
dest_dir = "/Users/karinabao/github-projects/ritter-ipo-analysis/"
today = datetime.today().strftime('%Y%m%d')
file_path = "ipo-analysis.xlsx"

# Load the Excel file
ipo_data = pd.read_excel(file_path)

# Filter the data for IPOs in 2023
ipos_2023 = ipo_data.loc[(ipo_data['offer date'] >= 20100000)  & ((ipo_data['VC'] == 1) |(ipo_data['VC'] == 2))]

# Display the filtered data
ipos_2023_list = ipos_2023[['IPO name', 'ticker', 'offer date', 'VC']]
print("List of IPOs in 2023:")
print(ipos_2023_list)

csv_file_path = f"{dest_dir}{today}-ipos-2010-2023.csv"
ipos_2023_list.to_csv(csv_file_path, index=False)



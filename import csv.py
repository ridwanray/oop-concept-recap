

import json
import csv
 
data = [
    {'date': '2021-11-01', 'PMS_N': None, 'PMS_L': None, 'AGO_N': None, 'AGO_L': None, 'DPK_N': None, 'DPK_L': None},
     {'date': '2021-11-02', 'PMS_N': None, 'PMS_L': None, 'AGO_N': None, 'AGO_L': None, 'DPK_N': None, 'DPK_L': None}, 
     {'date': '2021-11-03', 'PMS_N': None, 'PMS_L': None, 'AGO_N': None, 'AGO_L': None, 'DPK_N': None, 'DPK_L': None}, {'date': '2021-11-04', 'PMS_N': None, 'PMS_L': None, 'AGO_N': None, 'AGO_L': None, 'DPK_N': None, 'DPK_L': None}, {'date': '2021-11-05', 'PMS_N': None, 'PMS_L': None, 'AGO_N': None, 'AGO_L': None, 'DPK_N': None, 'DPK_L': None}]
#
 
# Opening JSON file and loading the data
# into the variable data
# with open('data.json') as json_file:
#     data = json.load(json_file)
 
employee_data = data
 
# now we will open a file for writing
data_file = open('data_file.csv', 'w')
 
# create the csv writer object
csv_writer = csv.writer(data_file)
 
# Counter variable used for writing
# headers to the CSV file
count = 0
 
for emp in employee_data:
    if count == 0:
 
        # Writing headers of CSV file
        header = emp.keys()
        csv_writer.writerow(header)
        count += 1
 
    # Writing data of CSV file
    print(emp.values())
    if emp.values() is None:
        print('value is empthy')
    csv_writer.writerow(emp.values() or 1)
 
data_file.close()
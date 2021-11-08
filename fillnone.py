import csv
mydata = [
    {'date': '2021-07-14', 'PMS_N': 24800.0, 'PMS_L': 740.0, 'AGO_N': None, 'AGO_L': None, 'DPK_N': None, 'DPK_L': None}, 
    {'date': '2021-07-15', 'PMS_N': None, 'PMS_L': None, 'AGO_N': None, 'AGO_L': None, 'DPK_N': None, 'DPK_L': None},
    {'date': '2021-07-16', 'PMS_N': None, 'PMS_L': None, 'AGO_N': None, 'AGO_L': None, 'DPK_N': None, 'DPK_L': None}
     ]

headers = mydata[0].keys()



    
for eachDateDataDict in mydata:
    for key, val in eachDateDataDict.items():
        if val is None:
           eachDateDataDict[key] = "0.00"
        
with open('email-sales-report.csv', 'w', newline='')  as salesReport:
    dict_writer = csv.DictWriter(salesReport, headers)
    dict_writer.writeheader()
    dict_writer.writerows(mydata)
# print('my-data::',mydata)

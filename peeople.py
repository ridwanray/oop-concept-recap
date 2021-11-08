import csv
toCSV = [{'name':'bob','age':25,'weight':None},
         {'name':'jim','age':31,'weight':180}]
# keys = toCSV[0].keys()


# with open('people.csv', 'w', newline='')  as output_file:
#     dict_writer = csv.DictWriter(output_file, keys,restval='90')
#     dict_writer.writeheader()
#     dict_writer.writerows(toCSV)

# with open('dict.csv', 'w') as csv_file:  
#     writer = csv.writer(csv_file)
#     for key, value in toCSV.items():
#        writer.writerow([key, value])

import csv
import os
# #file_to_load = 'Resources/election_results.csv'

csvpath = os.path.join('Resources','election_results.csv')
    
# with open(file_to_load) as Election_data:
#     print(Election_data)
# file_to_save = os.path.join('Analysis','election_analysis.txt')
# with open(csvpath) as election_data:
#     # txt_file.write('Counties in the Election\n---------------------\nArapahow\nDenver\nJefferson')
#     File_reader= csv.reader(election_data)
# for row in File_reader:
#     Print(row)

election_data=open(csvpath)
csv_reader=csv.reader(election_data)
headers=next(csv_reader)
# for row in csv_reader:
print(headers)

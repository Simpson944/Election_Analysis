import csv
import os
# #file_to_load = 'Resources/election_results.csv'

csvpath = os.path.join('Resources','election_results.csv')
    
# with open(file_to_load) as Election_data:
#     print(Election_data)
file_to_save = os.path.join('Analysis','election_analysis.txt')
# with open(csvpath) as election_data:
#     # txt_file.write('Counties in the Election\n---------------------\nArapahow\nDenver\nJefferson')
#     File_reader= csv.reader(election_data)
# for row in File_reader:
#     Print(row)
total_votes=0
candidate_options=[]
candidate_votes={}
Winning_Candidate=""
Winning_count=0
Winning_Percentage=0
election_data=open(csvpath)
csv_reader=csv.reader(election_data)
headers=next(csv_reader)
for row in csv_reader:
    candidate_name=row[2]
    if candidate_name not in candidate_options:
        candidate_options.append(candidate_name)
        candidate_votes [candidate_name]=0
    candidate_votes [candidate_name]+=1
    total_votes +=1
with open(file_to_save, "w") as txt_file:
    election_results= (
        f'\nElection Results\n'
        f'--------------------\n'
        f'Total Votes: {total_votes:,}\n'
        f'--------------------\n')
    print(election_results, end="")
    txt_file.write(election_results)
        
    for candidate_name in candidate_votes:
        votes=candidate_votes [candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        
        #print(f"{candidate_name}:{vote_percentage:.1f}% ({votes:,})\n")  
        if (votes > Winning_count) and (vote_percentage > Winning_Percentage):
            Winning_count = votes
            Winning_Percentage = vote_percentage
            Winning_Candidate = candidate_name
        Winning_Candidate_Summary= (
            f"------------------------\n"
            f'Winner: {Winning_Candidate}\n'
            f'Winning Vote count: {Winning_count:,}\n'
            f'Winning Percentage: {Winning_Percentage:.1f}%\n'
            f'-------------------------\n')
    #print(Winning_Candidate_Summary)      
        candidate_results=(f"{candidate_name}:{vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
    txt_file.write(Winning_Candidate_Summary)

    
    
    #total_votes +=1
#print (total_votes)
    
import os
import csv


total_votes=0                                                           #Total votes by all candidates
candidate_name=[]                                                       #list for candidate name
vote=[]                                                                 #total votes for indivisual candidates
vote_percent=[]                                                         #vote percentage for indivisual candidates

os.chdir(os.path.dirname(__file__))                                     # Change directory to the directory of current python script


csvpath = os.path.join("Resources", "election_data.csv")                  # Path to collect data from the Resources folder


with open (csvpath,'r')as csvfile:                                      #Reading the CSV file
      csvreader=csv.reader(csvfile,delimiter=',')
      header_row=next(csvreader)                                        #Store header row
      

      for line in csvreader:                                            #Iterating through each row of the CSV file
          
        if line[2] not in candidate_name:                               #Check for candidate, if not in list, add them and add the vote count as well for the occurance
            candidate_name.append(line[2])
            vote.append(1)
        else:                                                           #If the candidate is in ablove list, count the vote occurance
            index = candidate_name.index(line[2])
            vote[index] += 1

        total_votes += 1                                                #total vote count

        
      for v in vote:                                                   #Calculating the percentage of votes for each candidate and rounding off to three decimal
          percent=round(((v/total_votes)*100),3)
          vote_percent.append(percent)

      winner_index = vote.index(max(vote))                              #Determining the winner
      winner = candidate_name[winner_index]

print("Election Results")                                                #Prinitng the election results

print("-----------------------------------------------------------------")

print("Total Votes: " + str(total_votes))

print("-----------------------------------------------------------------")

for i in range(len(candidate_name)):
    print(f"{candidate_name[i]}: {vote_percent[i]}%  ({vote[i]})")

print("-----------------------------------------------------------------")

print("Winner: " + str(winner))

print("-----------------------------------------------------------------")



# Output the election results to text file named electionresults.txt

res_file = os.path.join("Analysis", "electionresults.txt")
with open(res_file, "w") as file:

 file.write("Election Results" + "\n")

 file.write("-----------------------------------------------------------" + "\n")

 file.write("Total Votes: " + str(total_votes) + "\n")

 file.write("-----------------------------------------------------------" + "\n")

 for i in range(len(candidate_name)):
    
    file.write(f"{candidate_name[i]} :  {vote_percent[i]}%  ({vote[i]})"+ "\n")
               
 file.write("-----------------------------------------------------------" + "\n")

 file.write("Winner: " + str(winner) + "\n")

 file.write("-----------------------------------------------------------" + "\n")



file.close()
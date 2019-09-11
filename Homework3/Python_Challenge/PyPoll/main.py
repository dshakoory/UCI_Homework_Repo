#import the libraries
import os
import csv

# Opening the CSV file and ask it to read 
poll= os.path.join("polldata.csv")
# Opening the CSV file and ask it to read a text file to write

with open(poll, 'r') as csvfile,\
	open('electiondata.txt', 'w') as textfile:

#ed defined as Election Data
	ed = csv.reader(csvfile, delimiter=",")
#edh defined as eleciton data header- skipping the header with next	
	edh = next(ed)

	#storing the results in the dictionaries
	cvotes = {} #cvotes is defining the votes for candidates 
    #{} will store them in a dictionary
	percent = {} #percent is defining the percentage of candidates
     #{} will store them in a dictionary
	votect = 0 #votect is defining the count of votes
	
	# we are looping throgh each row of data in election data
    #i is defined as row number
	for i in ed:
		#counting the votes
		if i[2] not in cvotes:
			cvotes[i[2]] = 1
		else:
			cvotes[i[2]] =cvotes[i[2]]+ 1


		#loopinf through and calculating the total number of votes
		votect =votect + 1

	# The total number of votes each candidate won
	winner = max(cvotes.values())

	# list of candidates who got votes
	clist = list(cvotes.keys())
	clist_votes = list(cvotes.items())

	# Loop through candidates in the list of tuples we have created earlier
	for candidates, votes in clist_votes:

		# calculate the percentage of votes to store in a dictionary in a percentage format
		votespct = "{0:.0f}".format((votes/votect)*100)
		percent[candidates] = votespct


		# winner of the whole election (The winner of the election based on popular vote)
		if votes == winner:
			popularvotes = candidates

	
	election_results = f"""
	Final Election Results
	Total Votes = {votect}
	{clist[0]}: {percent[clist[0]]}% ({cvotes[clist[0]]})
	{clist[1]}: {percent[clist[1]]}% ({cvotes[clist[1]]})
	{clist[2]}: {percent[clist[2]]}% ({cvotes[clist[2]]})
	{clist[3]}: {percent[clist[3]]}% ({cvotes[clist[3]]})
	Winner: {popularvotes}"""


	#adding the results to the text file 
	textfile.write(election_results)
	print(election_results)
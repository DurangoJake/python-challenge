import os
import csv


election =('election_data.csv')



with open(election) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    vote_counter1 = 0
    vote_counter2 = 0
    vote_counter3 = 0
    vote_counter4 = 0

    
    
    
    votedict = {

    }
   
    name1 = "Khan"
    name2 = "Correy"
    name3 = "Li"
    name4 = "O'Tooley"


    canidate = [name1, name2, name3, name4]
    



    for row in csvreader:
        if name1 in row:

            vote_counter1 = vote_counter1 + 1
        elif name2 in row:

            vote_counter2 = vote_counter2 + 1
        elif name3 in row:

            vote_counter3 = vote_counter3 + 1
        elif name4 in row:

            vote_counter4 = vote_counter4 + 1
    

    
# i thought about using a dict but didnt get it to work
    #votedict.update({ name1: vote_counter1, name2: vote_counter2, name3: vote_counter3, name4: vote_counter4})
    #winner = max(votedict)
    total_votes = vote_counter1 + vote_counter2 + vote_counter3 + vote_counter4
    votes = [vote_counter1, vote_counter2, vote_counter3, vote_counter4]
    
    winner_count = max(votes)
    winner_index = votes.index(winner_count)
    winner = canidate[winner_index]
    print (winner_index)
    print(votes)


    per_vote1 = (vote_counter1 / total_votes) * 100
    per_vote2 = (vote_counter2 / total_votes) * 100
    per_vote3 = (vote_counter3 / total_votes) * 100
    per_vote4 = (vote_counter4 / total_votes) * 100

    print("Election Results")
    print ("-" * 20)

    print ("Total Votes: ", total_votes)
    print ("-" * 20)
    print (name1 , per_vote1 , "%",vote_counter1)
    print (name2 , per_vote2 , "%",vote_counter2)
    print (name3 , per_vote3 , "%", vote_counter3)
    print (name4 , per_vote4 , "%", vote_counter4)

    print ("-" * 20)
    print("Winner is: ", winner)
    



        

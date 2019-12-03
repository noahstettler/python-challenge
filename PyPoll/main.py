import csv

# Text File
f = open("Election.txt", "w+")

with open("election_data.csv") as in_file:
    csv_reader = csv.reader(in_file)
    header = next(csv_reader)
    data = list(csv_reader)
    
    print("Election Results")

    # Number of Votes Cast
    num_votes = len(data)    
    str_votes = "Number of Votes: " + str(num_votes)
    print(str_votes)

    # Number of Votes per Candiate
    candiates = []
    Khan_votes = 0
    Correy_votes = 0
    Li_votes = 0
    OTooley_votes = 0
    for i in range(1, len(data)):
        candiate = str(data[i][2])
        candiates.append(candiate)
        
    for candiate in candiates:
        if candiate == "Khan":
            Khan_votes += 1
        if candiate == "Correy":
            Correy_votes += 1
        if candiate == "Li":
            Li_votes += 1  
        if candiate == "O'Tooley":
            OTooley_votes += 1  

    # Percent of the Vote
    Khan_percent = (Khan_votes/num_votes) * 100                
    Correy_percent = (Correy_votes/num_votes) * 100
    Li_percent = (Li_votes/num_votes) * 100
    OTooley_percent = (OTooley_votes/num_votes) * 100  

    # Election Winner
    winner = max(Khan_votes,Correy_votes,Li_votes,OTooley_votes)
    winner_name = ""
    if winner == Khan_votes:
        winner_name = "Khan"
    if winner == Correy_votes:
        winner_name = "Correy"  
    if winner == Li_votes:
        winner_name = "Li"  
    if winner == OTooley_votes:
        winner_name = "O'Tooley"

    # Printing
    str_Khan = "Khan: " + str(Khan_percent) + "%, " + str(Khan_votes) + " Votes"
    str_Correy = "Correy: " + str(Correy_percent) + "%, " + str(Correy_votes) + " Votes"           
    str_Li = "Li: " + str(Li_percent) + "%, " + str(Li_votes) + " Votes"
    str_OTooley = "O'Tooley: " + str(OTooley_percent) + "%, " + str(OTooley_votes) + " Votes"
    print(str_Khan)
    print(str_Correy)
    print(str_Li)
    print(str_OTooley)
    print("Winner:" + winner_name)


f.close

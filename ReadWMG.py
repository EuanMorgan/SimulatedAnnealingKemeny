import Results

class ReadWMG:

    def __init__(self):
        self.res = None
        self.filename = input("Enter a filename (defaults to 1994_Formula_One.wmg if none specified)")
        if self.filename == "":
            self.filename = "1994_Formula_One.wmg"
        
        file = open(self.filename)
        
        num_participants = int(file.readline().replace('\n',"").strip())

        participants = {}

        for i in range(0,num_participants):
            line = file.readline().replace("\n","").strip().split(",")
           
            participants[int(line[0])] = line[1]

        self.res = Results.Results(participants)

        num_matchups = int(file.readline().replace("\n","").split(",")[2])
        for i in range(0,num_matchups):
            line = file.readline().strip().replace("\n","").split(",")
            self.res.add_matchup(int(line[1]),int(line[2]),int(line[0]))
            
    
    def ret(self):
        return self.res
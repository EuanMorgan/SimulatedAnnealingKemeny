class Results:
    
    def __init__(self,participants):
        self.participants = participants
        self.matchups = {}
 

    def print_matchups(self):
        print(self.matchups)

    def add_matchup(self,p1,p2,score):
        self.matchups[(p1,p2)] = score

    def get_matchup(self,p1,p2):
       
        score = self.matchups.get((p1, p2))

        if score != None:
            return score
        
        #try other way around, since matchup may only be stored for (1,2) but not (2,1) for example...

        score = self.matchups.get((p2, p1))

        if score != None:
            return -score

        return None

    def get_name(self,p):
        return self.participants[p]

import time
import random
class Ranking:

    def __init__(self,results,ranking, *args):
        self.results = results
        self.ranking = ranking
        self.length = len(self.ranking)
        if args:
            self.score = args[0]
        else:
            self.score = self.calculate_cost()
     
    
    def get_score(self):
        return self.score


    def generate_neighbour(self):
        old_rank = random.randrange(0,self.length)
        new_rank = 0
        while True:
            new_rank = random.randrange(0,self.length)
            difference = abs(new_rank-old_rank)

            if not (difference == 0):
                break
        neighbour_rank = self.ranking.copy()

        neighbour_rank.insert(new_rank,neighbour_rank.pop(old_rank))
        abs(1-1)
        return Ranking(self.results,neighbour_rank,self.calc_neighbour_cost(old_rank,new_rank))

    def calc_neighbour_cost(self,old,new):
        participant = self.ranking[old]
        score = self.get_score()
     
        move = None
        i = 0
        if new < old:
            move = 1
            i = new - 1
        else:
            move = -1
            i = new + 1
        

        while i != old:
            i+=move
            s = self.results.get_matchup(participant, self.ranking[i])
            if s == None:
                continue
            if (old > i) and (s > 0):
                score -= abs(s)
            else:
                score += abs(s)
            
        return score
            

    def calculate_cost(self):
        score = 0

        for i in range(0,self.length):
            for j in range(0,self.length):
                if i == j:
                    continue
                weight = self.results.get_matchup(i+1,j+1)
               
                if weight == None:
                    continue
                    
                if weight > 0 and self.ranking.index(i+1) > self.ranking.index(j+1):
                    score+=weight
      
        return score
    
    def out(self):
        string = "PLACE  NAME\n"
        for i in self.ranking:
            string += "    " + str(self.ranking.index(i)+1) + "  " + self.results.get_name(i) + "\n"
        
        return string
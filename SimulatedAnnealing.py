import Ranking
import random
import math
class SimulatedAnnealing:
    def __init__(self,initial_ranking):
        self.initial_ranking = initial_ranking
        self.T = 1
        self.TL = 20
        self.nums_non_improve = 10000

    def cool(self):
        self.T = 0.95*self.T
    
    def run(self):
        best_rank = self.initial_ranking
        current_rank = best_rank

        nums = 0

        while self.nums_non_improve > nums:
            for i in range(0,self.TL):
                
                neighbour_rank = current_rank.generate_neighbour()
                delta_cost = neighbour_rank.get_score() - current_rank.get_score()
                
                if delta_cost <= 0:
                    current_rank = neighbour_rank

                    if current_rank.get_score() < best_rank.get_score():
                        
                        best_rank = current_rank
                    else:
                        nums+=1
                else:
                    q = random.random()
                    prob = math.pow(math.e,-delta_cost/self.T)
                    if prob > q:
                        current_rank = neighbour_rank
                    nums+=1

        
            
            self.cool()
        return best_rank
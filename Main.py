import ReadWMG
import Ranking
import SimulatedAnnealing
import time
from matplotlib import pyplot
import numpy
scores = []
times = []

class Main:

    def __init__(self):
        
        a = ReadWMG.ReadWMG()
        start = time.time()
        results = a.ret()
        initial_ranking = Ranking.Ranking(results,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 
        29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45,46])

        sa = SimulatedAnnealing.SimulatedAnnealing(initial_ranking)
        
        final_rank = sa.run()
        end = time.time()
        
        
        print(final_rank.out())
        print("SCORE {}".format(final_rank.calculate_cost()))
        print("RUNTIME: " + str(round((end-start)*1000,2)) + "MS")
        # times.append(round((end-start)*1000,2))
        # scores.append(final_rank.calculate_cost())


a = Main()
# for i in range(0,500):
#     a = Main()

# x = times
# y = scores

# bins = numpy.linspace(0,10,100)
# pyplot.hist(x,bins=30,label='Run time (ms)')
# pyplot.hist(y,bins=30,label='Score')
# pyplot.legend(loc='upper right')
# pyplot.ylabel('occurences')

# pyplot.show()


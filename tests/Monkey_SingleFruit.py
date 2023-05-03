"""

Single Fruit Test

"""
#import pyNN.spiNNaker as sim
import pyNN.nest as sim

from monkeyProblem import MonekyProblem

sim.setup(timestep=1.0,min_delay=1.0,max_delay=1.0, debug=0)

#mp = MonekyProblem(sim, "spinnaker")
mp = MonekyProblem(sim, "nest")

mp.narc.addFact("chairAt", (1,))
mp.narc.addFact("fruit", ("banana",0))

mp.narc.apply()

sim.run(200)

mp.printSpikes()

sim.end()
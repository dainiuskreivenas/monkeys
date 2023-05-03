"""

Two Fruit Test 
Fruits:
 1: Banana, 0;
 2: Apple, 1.
Chair:
    1: 2

"""

#import pyNN.spiNNaker as sim
import pyNN.nest as sim
from monkeyProblem import MonekyProblem

sim.setup(timestep=1.0,min_delay=1.0,max_delay=1.0, debug=0)

#mp = MonekyProblem(sim, "spinnaker")
mp = MonekyProblem(sim, "nest")

mp.narc.addFact("chairAt", (2,))
mp.narc.addFact("fruit",("banana",0))
mp.narc.addFact("fruit",("apple",1))

mp.narc.apply()

sim.run(200)

mp.printSpikes()

sim.end()

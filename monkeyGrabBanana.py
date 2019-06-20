"""

Single Fruit Test

"""
#import pyNN.spiNNaker as sim
import pyNN.nest as sim

from rbs.rbs import RBS

sim.setup(timestep=1.0,min_delay=1.0,max_delay=1.0, debug=0)

#rbs = RBS(sim, "spinnaker")
rbs = RBS(sim, "nest")

rbs.addRule(
    (
        "MonkeyCanReach",
        (
            [
                (True, "MonkeyCanReach", ("?type",),"b")
            ],
            [
                ("assert",("MonkeyGrab", ("?type",))),
                ("retract", "b")
            ]
        )
    )
)

rbs.addFact(("MonkeyCanReach",("banana",)))

sim.run(50)

rbs.printSpikes()

sim.end()
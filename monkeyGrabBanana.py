"""

Single Fruit Test

"""
#import pyNN.spiNNaker as sim
import pyNN.nest as sim

from rbs import FSAHelperFunctions
from rbs import NealCoverFunctions
from rbs import RuleBasedSystemBuilder

sim.setup(timestep=1.0,min_delay=1.0,max_delay=1.0, debug=0)

neal = NealCoverFunctions("nest", sim)
fsa = FSAHelperFunctions("nest", sim, neal)

rbsBuilder = RuleBasedSystemBuilder(sim, "nest", fsa)
rbs = rbsBuilder.build()

rbs.addRule(   
    "MonkeyCanReach",
    [
        (True, "MonkeyCanReach", ("?type",),"b")
    ],
    [
        ("assert",("MonkeyGrab", ("?type",))),
        ("retract", "b")
    ]
)

rbs.addFact("MonkeyCanReach", ("banana",))

neal.nealApplyProjections()

sim.run(50)

rbs.printSpikes()

sim.end()
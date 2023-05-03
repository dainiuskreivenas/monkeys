"""

Single Fruit Test

"""
#import pyNN.spiNNaker as sim
import pyNN.nest as sim

from rbs.stateMachineClass import FSAHelperFunctions
from rbs.nealCoverClass import NealCoverFunctions
from rbs.narcBuilder import NeuralCognitiveArchitectureBuilder

sim.setup(timestep=1.0,min_delay=1.0,max_delay=1.0, debug=0)

neal = NealCoverFunctions("nest", sim)
fsa = FSAHelperFunctions("nest", sim, neal)
narc = NeuralCognitiveArchitectureBuilder("nest", sim, fsa, neal).build()

narc.addRule(
    "MonkeyCanReach",
    [
        (True, "MonkeyCanReach", ("?type",),"b")
    ],
    [
        ("assert",("MonkeyGrab", ("?type",))),
        ("retract", "b")
    ]
)

narc.addFact("MonkeyCanReach", ("banana",))

narc.apply()

sim.run(50)

narc.printSpikes()

sim.end()
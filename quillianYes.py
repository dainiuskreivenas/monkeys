"""

Simple test for monkey reach using associations

"""
import pyNN.nest as sim

from rbs.rbs import RuleBasedSystem
from rbs.association.association import Association

sim.setup(timestep=1.0,min_delay=1.0,max_delay=1.0, debug=0)

simTime = 100

association = Association(sim, "nest")
association.useBases("bases")
association.build()

rbs = RuleBasedSystem(sim, "nest")
rbs.useAssociation(association)
rbs.build()
    

rbs.addRule(
    "askIsChildParent",
    [
        (True, "question", ("is", "?subType", "?superType"), "f1")
    ],
    [
        ("base", "?subType"),
        ("prime", "base")
    ]
)

rbs.addRule(
    "resolveIsChildParent",
    [
        (True, "question", ("is", "?subType", "?superType"), "f1"),
        ("base", "?subType", "f2"),
        ("base", "?superType", "f3"),
        ("prime", "base", "f4")
    ],
    [
        ("assert", ("isType", ("?subType", "?superType"))),
        ("retract", "f1"),
        ("retract", "f2"),
        ("retract", "f3"),
        ("retract", "f4")
    ]
)

rbs.addFact("question", ("is", "canary", "bird"))

## Run
sim.run(simTime)

## Print data
rbs.printSpikes()

sim.end()
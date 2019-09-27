"""

Simple test for monkey reach using associations

"""
import pyNN.nest as sim
from rbs import FSAHelperFunctions
from rbs import Association
from rbs import RuleBasedSystemBuilder

sim.setup(timestep=1.0,min_delay=1.0,max_delay=1.0, debug=0)

simTime = 100

fsa = FSAHelperFunctions(sim, "nest")

association = Association(sim, "nest")
association.useBases("bases")
association.build()

rbsBuilder = RuleBasedSystemBuilder(sim, "nest", fsa)
rbsBuilder.useAssociation(association)
rbs = rbsBuilder.build()

rbs.addRule(
    "askIsChildParent",
    [
        (True, "question", ("is", "?subType", "?superType"), "f1")
    ],
    [
        ("base", "?subType"),
        ("link", ("base", "?subType", "query")),
        ("link", ("base", "?superType", "query")),
        ("prime", "base")
    ]
)

rbs.addRule(
    "resolveIsChildParent",
    [
        (True, "question", ("is", "?subType", "?superType"), "f1"),
        ("link", ("base", "?superType", "query"), "f2"),
    ],
    [
        ("assert", ("isType", ("?subType", "?superType"))),
        ("retract", "f1"),
        ("retract", "f2")
    ]
)

rbs.addRule(
    "cleanupIsChildParent",
    [
        (True, "isType", ("?subType", "?superType"), "f1"),
        ("link", ("base", "?subType", "query"), "f2"),
        ("prime", "base", "f3")
    ],
    [
        ("retract", "f1"),
        ("retract", "f2"),
        ("retract", "f3")
    ]
)

rbs.addFact("question", ("is", "canary", "animal"))

## Run
sim.run(simTime)

## Print data
rbs.printSpikes()

sim.end()

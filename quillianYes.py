"""

Simple test for monkey reach using associations

"""
import pyNN.nest as sim
from rbs import FSAHelperFunctions
from rbs import NealCoverFunctions
from rbs import NeuralCognitiveArchitectureBuilder

sim.setup(timestep=1.0,min_delay=1.0,max_delay=1.0, debug=0)

simTime = 200

neal = NealCoverFunctions("nest", sim)
fsa = FSAHelperFunctions("nest", sim, neal)

narcBuilder = NeuralCognitiveArchitectureBuilder("nest", sim, fsa, neal)
narcBuilder.useBasesFile("bases")
narcBuilder.useRelationshipsFiles("props", "rels", "assocs")

narc = narcBuilder.build()

narc.addRule(
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

narc.addRule(
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

narc.addRule(
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

narc.addRule(
    "hasBaseOperationProperty",
    [
        (True, "question", ("does", "?base", "?rel", "?property"), "f1")
    ],
    [
        ("link", ("base", "?base", "stimulate")),
        ("link", ("relationship", "?rel", "stimulate")),
        ("prime", "property")
    ]
)

narc.addRule(
    "resolveBaseOperationProperty",
    [
        (True, "question", ("does", "?base", "?rel", "?property"), "f1"),
        ("property", "?property", "f2"),
        ("link", ("base", "?base", "stimulate"), "f3"),
        ("base", "?base", "f4"),
        ("link", ("relationship", "?rel", "stimulate"), "f5"),
        ("relationship", "?rel", "f6"),
        ("prime", "property", "f7")
    ],
    [
        ("assert", ("is", ("?base", "?rel", "?property"))),
        ("retract", "f1"),
        ("retract", "f3"),
        ("retract", "f5"),
        ("retract", "f7"),
    ]
)

narc.addFact("question", ("does", "canary", "eats", "food"))

narc.addFact("question", ("is", "canary", "animal"))

neal.nealApplyProjections()

## Run
sim.run(simTime)

## Print data
narc.printSpikes()

sim.end()

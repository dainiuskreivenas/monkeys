"""

Simple test for monkey reach using associations

"""
import pyNN.nest as sim
from rbs.rbs import RuleBasedSystem

sim.setup(timestep=1.0,min_delay=1.0,max_delay=1.0, debug=0)

simTime = 100

rbs = \
    RuleBasedSystem(sim, "nest") \
        .useBases("bases") \
        .build(simTime)
    
rbs.addRule(
    (
        "grab-fruit-mammal",
        (
            [
                (True, "can-reach", ("?animal", "?fruit"), "a"),
                ("IsA", "mammal")
            ],
            [
                ("assert", ("reaches", ("?animal", "climb"))),
                ("retract", "a")
            ]
        )
    )
)

rbs.addRule(
    (
        "grab-fruit-bird",
        (
            [
                (True, "can-reach", ("?animal", "?fruit",), "a"),
                ("IsA", "bird")
            ],
            [
                ("assert", ("reaches", ("?animal", "fly"))),
                ("retract", "a")
            ]
        )
    )
)

rbs.addFact(("can-reach", ("monkey", "banana")))

## Activate Monkey

unit = rbs.association.inheritance.getUnitNumber("monkey")
primeTimes = [5]
primeArray = {'spike_times': [primeTimes]}
generator = sim.Population(1, sim.SpikeSourceArray, primeArray)
rbs.fsa.turnOnStateFromSpikeSource(generator, rbs.association.topology.neuralHierarchyTopology.cells, unit*10)

## Run
sim.run(simTime)

## Print data
rbs.printSpikes()

sim.end()
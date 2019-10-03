from rbs import FSAHelperFunctions
from rbs import NealCoverFunctions
from rbs import RuleBasedSystemBuilder

class MonekyProblem:

    def __init__(self, sim, simulator):
        self.neal = NealCoverFunctions(simulator, sim)
        self.fsa = FSAHelperFunctions(simulator, sim, self.neal)

        self.rbs = RuleBasedSystemBuilder(sim, simulator, self.fsa).build()

        self.rbs.addRule(
            "eatFruit",
            [
                (True, "monkey-has", ("?type",), "a")
            ],
            [
                ("assert", ("monkey-ate", ("?type",))),
                ("retract", "a")
            ]
        )

        self.rbs.addRule(
            "monkeyHasFruit",
            [
                (True, "chairAt", ("?pos",), "a"),
                (True, "fruit", ("?type","?pos"),"b")
            ],
            [
                ("assert",("monkey-has", ("?type",))),
                ("retract", "b")
            ]
        )

        self.rbs.addRule(
            "pushChair", 
            # if
            [
                (True,  "fruit", ("?","?pos"), "a"),
                (False, "chairAt", ("?pos",), "b")
            ],
            # then
            [
                ("assert", ("chairAt", ("?pos",))),
                ("retract", "b")
            ]
        )

    def printSpikes(self):
        self.rbs.printSpikes()

    

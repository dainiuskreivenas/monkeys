from rbs import FSAHelperFunctions
from rbs import NealCoverFunctions
from rbs import NeuralCognitiveArchitectureBuilder

class MonekyProblem:

    def __init__(self, sim, simulator):
        self.neal = NealCoverFunctions(simulator, sim)
        self.fsa = FSAHelperFunctions(simulator, sim, self.neal)
        self.narc = NeuralCognitiveArchitectureBuilder(simulator, sim, self.fsa, self.neal).build()

        self.narc.addRule(
            "eatFruit",
            [
                (True, "monkey-has", ("?type",), "a")
            ],
            [
                ("assert", ("monkey-ate", ("?type",))),
                ("retract", "a")
            ]
        )

        self.narc.addRule(
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

        self.narc.addRule(
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
        self.narc.printSpikes()

    

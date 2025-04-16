# Exercice https://courses.21-learning.com/runestone/books/published/oci-2224-donc/classic-problems/01-knapsack-short.html#force-brute

from itertools import product
from more_itertools import dotproduct

from knapsack import KnapsackInstance, KnapsackSolver

class GloutonKnapsackSolver(KnapsackSolver):

    
    def __init__(self, instance:KnapsackInstance) -> None:
        # TODO: write the constructor by calling the parent class constructor
        super().__init__(instance)
        self.iWV = [(i, (w, v)) for i, (w, v) in enumerate(zip(instance.W, instance.V))]
        self.iWV.sort(key=lambda x: x[1][1] / x[1][0], reverse=True)

    
    def solve(self) -> tuple[int, ...]:
        # solve by greedy algorithm
        result = [0] * len(self._inst.W)

        for i, (w, v) in self.iWV:
            if self._inst.C >= w:
                self._inst.C -= w
                result[i] = 1
        
        return tuple(result)

        

try:
    import doctest

    doctest.testmod()
except:
    print("Unable to load doctests")
# Exercice https://courses.21-learning.com/runestone/books/published/oci-2224-donc/classic-problems/01-knapsack-short.html#force-brute

from itertools import product
from more_itertools import dotproduct

from knapsack import KnapsackInstance, KnapsackSolver

class GloutonKnapsackSolver(KnapsackSolver):
    """
    >>> kp = KnapsackInstance(W=[13, 13, 13, 10, 24, 11], V=[2600, 2600, 2600, 500, 4500, 960], C=50)
    >>> bfs = BruteforceKnapsackSolver(kp)
    >>> Xopt = bfs.solve()
    >>> Xopt in [(0, 1, 1, 0, 1, 0), (1, 0, 1, 0, 1, 0), (1, 1, 0, 0, 1, 0)]
    True
    >>> bfs.value(Xopt)
    9700
    >>> bfs.weight(Xopt)
    50
    >>> bfs.weight(Xopt) <= bfs._inst.C
    True

    """
    
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
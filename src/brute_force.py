# Exercice https://courses.21-learning.com/runestone/books/published/oci-2224-donc/classic-problems/01-knapsack-short.html#force-brute

from itertools import product
from more_itertools import dotproduct

from knapsack import KnapsackInstance, KnapsackSolver

class BruteforceKnapsackSolver(KnapsackSolver):
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
        super.__init__()

    
    def solve(self) -> tuple[int, ...]:
        # solve by brute force

        possibilities = product((0,1), repeat=len(self._inst.W))
        gain_possibility_tuples = ((dotproduct(possibility, self._inst.V), possibility) for possibility in possibilities if dotproduct(possibility, self._inst.W) <= self._inst.C)
        
        def get_max_gain_possibility(gain_possibility_tuples:tuple[int, tuple[int, ...]]) -> tuple[int, ...]:
            max_gain = 0
            best_possibility = None
            for gain, possibility in gain_possibility_tuples:
                if gain > max_gain:
                    max_gain = gain
                    best_possibility = possibility
            return best_possibility

        return get_max_gain_possibility(gain_possibility_tuples)
import os
from abc import abstractmethod, ABC

class KnapsackInstance:
    '''
    >>> filepath = os.path.join('test_instances', 'toy-instance')
    >>> kp = KnapsackInstance.load_from_file(filepath)
    >>> kp
    KnapsackInstance(W=[13, 13, 13, 10, 24, 11], V=[2600, 2600, 2600, 500, 4500, 960], C=50)
    
    '''
    @staticmethod
    def load_from_file(filepath: str) -> 'KnapsackInstance':
        '''
        '''
        W: list[int] = []
        V: list[int] = []
        C: int = 0
        
        # add code here to load instances
        ...
        
        return KnapsackInstance(W, V, C)

    def __init__(self, W: list[int], V: list[int], C: int) -> None:
        self.W: list[int] = W
        self.V: list[int] = V
        self.C: int = C
        self.size: int = len(W)

    def __repr__(self):
        return f"{__class__.__name__}(W={self.W}, V={self.V}, C={self.C})"


class KnapsackSolver(ABC):
    '''
    '''
    
    def __init__(self, instance):
        self._inst = instance
        # 0-1 decision variables
        self._X: list[int] = [0] * self._inst.size

    @abstractmethod
    def solve(self):
        '''
        Solves the loaded instance and returns the assignment to the decision
        variables
        '''
        pass
        
    @abstractmethod
    def volume(self, X: list[int]) -> int:
        '''
        Computes the total volume of the objects contained in the solution X
        '''
        pass
    
    @abstractmethod
    def value(self, X: list[int]) -> int:
        '''
        Computes the total value of the objects contained in the solution X
        '''
        pass
        

try:
    import doctest
    doctest.testmod()
except:
    print("Unable to load doctests")    
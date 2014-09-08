from rabbit.all import random as BaseRandom

class Random(BaseRandom):
    """Base Wrapper Class.
Implemented Wrappers:
 getstate
 setstate
 jumpahead
 getrandbits
 randrange
 randint
 choice
 shuffle
 sample
 random
 uniform
 call"""
    def getstate(self):
        """Wraps getpos."""
        return self.counter
    def setstate(self, state):
        """Wraps goto."""
        self.goto(state)
    def jumpahead(self, n):
        """Wraps advance."""
        self.advance(n)
    def getrandbits(self, k):
        """Wraps getbits."""
        return self.getbits(k)
    def randrange(self, start, stop):
        """Wraps chooserange."""
        return self.chooserange(start, stop)
    def randint(self, start, stop):
        """Wraps randrange."""
        return self.randrange(start, stop+1)
    def choice(self, seq):
        """Wraps choose."""
        return self.choose(seq)
    def shuffle(self, x):
        """Wraps scramble."""
        scrambled = self.scramble(x)
        while len(x) > 0:
            x.pop()
        for y in scrambled:
            x.append(y)
    def sample(self, population, k):
        """Wraps take."""
        return self.take(population, k)
    def random(self):
        """Wraps getfloat."""
        return self.getfloat()
    def uniform(self, a, b):
        """Wraps choosefloatrange."""
        return self.choosefloatrange(a, b)
    def call(self, *trash):
        """Wraps random."""
        return self.random()

class __rabbit__(Random):
    def __init__(self, e):
        return Random.__init__(self)

random = Random()

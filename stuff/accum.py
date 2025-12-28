class Accumulator:

    def __init__(self):
        self._count = 0
    
    @property
    def count(self) -> int:
        return self._count

    def add(self, more: int = 1):
        self._count += more
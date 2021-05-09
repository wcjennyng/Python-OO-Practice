"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    
    def __init__(self, start=0):
        """starts at 0"""
        self.start = self.new = start

    def generate(self):
        """generates next number"""
        self.new += 1
        return self.new - 1

    def reset(self):
        """resets to start"""
        self.new = self.start

    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.new}"
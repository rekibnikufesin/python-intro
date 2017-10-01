class Ball:
    def __init__(self, radius, color, weight):
        self.radius = radius
        self.color = color
        self.weight = weight

class Football:
    """A standard, regulation NFL ball"""
    def __init__(self, diameter, color, pressure):
        self.diameter = diameter
        self.color = color
        self.pressure = pressure

    def inflate(self, psi):
        self.pressure = self.pressure + psi

    def deflate(self, psi):
        self.pressure = self.pressure - psi

class PatriotsBall(Football):
    def inflate(self, psi):
        self.pressure = self.pressure - psi
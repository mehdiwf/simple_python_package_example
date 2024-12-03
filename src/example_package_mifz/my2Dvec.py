from math import sqrt


class My2DVector:
    def __init__(self, vx, vy):
        self.x = vx
        self.y = vy

    def show(self):
        print("vector: x=", self.x, ", y=", self.y)

    def get_norm(self):
        norm = sqrt(self.x**2 + self.y**2)
        return norm

    def normalize(self):
        norm = self.get_norm()
        self.x /= norm
        self.y /= norm

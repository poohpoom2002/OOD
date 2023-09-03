class Spherical:
    def __init__(self, r):
        self.radius = r

    def changeR(self, radius):
        self.radius = radius

    def findVolume(self):
        volume = (4 / 3) * 3.141592653589793238462643383279502884197169399375105820974944592307816406286 * self.radius ** 3
        return volume

    def findArea(self):
        area = 4 * 3.141592653589793238462643383279502884197169399375105820974944592307816406286 * self.radius ** 2
        return area

    def __str__(self):
        volume = self.findVolume()
        area = self.findArea()
        return f"Radius ={self.radius} Volumn = {volume} Area = {area}"

r1, r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(dir(R1))
print(R1)
R1.changeR(int(r2))
print(R1)


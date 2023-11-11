class Vector3D:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, Vector3D):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            return Vector3D(self.x * other, self.y * other, self.z * other)

    def __matmul__(self, other):
        return Vector3D(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)

    def display(self):
        print(f"({self.x}, {self.y}, {self.z})")

    def read(self):
        self.x = int(input("Enter x-coordinate: "))
        self.y = int(input("Enter y-coordinate: "))
        self.z = int(input("Enter z-coordinate: "))


v1 = Vector3D(2, 4, 1)
v1.display()

v2 = Vector3D()
v2.read()

v3 = Vector3D(1, 2, 3)

v4 = v1 + v2
v4.display()

a = v4 * v3
print(a)

v4 = v1 * 10
v4.display()

v4 = v1 @ v3
v4.display()

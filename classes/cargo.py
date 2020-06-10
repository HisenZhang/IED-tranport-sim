from classes.simobject import SimObject


class Cargo(SimObject):
    def __init__(self, content, weight, dimensions):
        self.content = content
        self.weight = weight
        self.dimensions = dimensions

        # TODO how to layout to load as much cargo as possible
        self.volume = dimensions[0] * dimensions[1] * dimensions[2]
        pass

    def update(self, step):
        # Cargo does not vary (and should not!) along the way
        pass

    def __str__(self):
        return "[Content] " + self.content + \
            "\n[Weight] " + str(self.weight) + \
            "\n[Dimensions(X,Y,Z)] " + \
            str(self.dimensions[0]) + "," + \
            str(self.dimensions[1]) + "," + \
            str(self.dimensions[2]) + "\n\n"

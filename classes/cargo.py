class Cargo:
    def __init__(self,content,weight,dimensions,qty=0):
        self.content = content
        self.weight = weight
        self.dimensions = dimensions

        # TODO how to layout to load as much cargo as possible
        self.volume = dimensions[0] * dimensions[1] * dimensions[2]
        self.quantity = qty # of boxes
        pass

    def setQuantity(self,qty):
        self.quantity = qty

    def __str__(self):
        return "[Content] " + self.content + \
                "\n[Weight] " + str(self.weight) + \
                "\n[Quantity] " + str(self.quantity) + \
                "\n[Dimensions(X,Y,Z)] " + \
                str(self.dimensions[0]) + ","+ \
                str(self.dimensions[1]) + ","+ \
                str(self.dimensions[2]) + "\n\n"
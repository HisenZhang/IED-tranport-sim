import copy


class SimObject(object):
    def __init__(self):
        pass

    def __mul__(self, qty):
        objectList = list()
        for _ in range(qty):
            objectList.append(copy.deepcopy(self))
        return objectList

    def _flattenList(self, inputList):
        flat_list = []
        for element in inputList:
            if isinstance(element, list):
                for item in element:
                    flat_list.append(item)
            else:
                flat_list.append(element)
        return flat_list

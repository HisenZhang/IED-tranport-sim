from classes.simobject import SimObject
from simulator.constant import CONSTANT
import math


class Coordinate(SimObject):
    def __init__(self, latitude, longtitude):
        self._latitude = latitude
        self._longtitude = longtitude

    def getCoordinate(self):
        return (self._latitude, self._longtitude)

    def getLatitude(self):
        return self._latitude

    def getLongtitude(self):
        return self._longtitude


class Path(SimObject):
    def __init__(self, coordinateList=[]):
        self._waypointList = list()
        self._waypointList.extend(coordinateList)
        pass

    def getDistance(self, waypoint1, waypoint2):

        # distance between two points over a sphere
        # https://en.wikipedia.org/wiki/Great-circle_distance

        lat1, lng1 = waypoint1.getCoordinate()
        lat2, lng2 = waypoint2.getCoordinate()
        radLat1 = math.radians(lat1)
        radLat2 = math.radians(lat2)

        a = radLat1 - radLat2
        b = math.radians(lng1) - math.radians(lng2)
        s = 2 * math.asin(math.sqrt(math.pow(math.sin(a/2), 2) +
                                    math.cos(radLat1) * math.cos(radLat2) * math.pow(math.sin(b/2), 2)))
        s = s * CONSTANT['EARTH_RADIUS']
        return s

    def getPathLength(self):

        # total length of the path
        # consecutive element pairing
        waypointPairs = [(self._waypointList[i], self._waypointList[i + 1])
                         for i in range(len(self._waypointList) - 1)]

        pathLength = float()
        for pairs in waypointPairs:
            pathLength += self.getDistance(pairs[0], pairs[1])
        return pathLength

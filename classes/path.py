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
    def __init__(self, coordinateList=[], inclineList=[]):
        self._waypointList = list()
        self._waypointList.extend(coordinateList)
        self._inclineList = list()
        self._inclineList.extend(self._flattenList(inclineList))
        self._location = 0.0
        self._segment = 0
        self._segmentPreCalcList = list()
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

        waypointPairs = self._getWaypointPairs()
        pathLength = float()
        for pairs in waypointPairs:
            pathLength += self.getDistance(pairs[0], pairs[1])
        return pathLength

    def update(self, distanceTraveled):
        self._location += distanceTraveled
        for cumulativeDistance in self._segmentPreCalcList:
            if self._location < cumulativeDistance:
                self._segment = self._segmentPreCalcList.index(
                    cumulativeDistance)
            break

    def getIncline(self):
        if len(self._inclineList) == 0:
            return 0
        else:
            return self._inclineList[self._segment]

    def getSegment(self):
        return self._segment

    def _segmentPreCalc(self):
        cumulativeDistance = float()
        waypointPairs = self._getWaypointPairs()
        for pair in waypointPairs:
            cumulativeDistance += self.getDistance(pair[0], pair[1])
            self._segmentPreCalcList.append(cumulativeDistance)

    def getWaypoint(self,index):
        return self._waypointList[index]

    def _getWaypointPairs(self):
        return [(self._waypointList[i], self._waypointList[i + 1])
                for i in range(len(self._waypointList) - 1)]

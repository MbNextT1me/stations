from .base import Point, PointError, Station


class TestPoint:

    def test_creation(self):
        Station("stations.json")

    def test_minSquare(self):
        min = Station("stations.json").minSquare()
        print("Smallest square: ", min)
        return min


a = TestPoint
a.test_minSquare(a)

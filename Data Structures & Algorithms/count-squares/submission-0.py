class CountSquares:

    def __init__(self):
        self.countPoints = defaultdict(int)
        self.points = []
        

    def add(self, point: List[int]) -> None:
        self.countPoints[tuple(point)] += 1
        self.points.append(point)
        

    def count(self, point: List[int]) -> int:
        res = 0
        qx, qy = point
        for x, y in self.points:
            if (abs(qx-x) != abs(qy-y)) or qx == x or qy == y:
                continue
            res += self.countPoints[(qx, y)] * self.countPoints[(x, qy)] 
        return res
        

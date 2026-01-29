# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        # If rectangle is invalid (no area), there are no ships
        if bottomLeft.x > topRight.x or bottomLeft.y > topRight.y:
            return 0

        # Prune: if Sea says there are no ships in this rectangle, stop immediately
        if not sea.hasShips(topRight, bottomLeft):
            return 0

        # Base case: rectangle is a single point
        # Since hasShips is True here, that point contains exactly 1 ship
        if bottomLeft.x == topRight.x and bottomLeft.y == topRight.y:
            return 1

        # Split rectangle into 4 smaller rectangles
        midx = (bottomLeft.x + topRight.x) // 2
        midy = (bottomLeft.y + topRight.y) // 2

        # Define corners for sub-rectangles:
        # 1) bottom-left quadrant
        bl1 = bottomLeft
        tr1 = Point(midx, midy)

        # 2) bottom-right quadrant
        bl2 = Point(midx + 1, bottomLeft.y)
        tr2 = Point(topRight.x, midy)

        # 3) top-left quadrant
        bl3 = Point(bottomLeft.x, midy + 1)
        tr3 = Point(midx, topRight.y)

        # 4) top-right quadrant
        bl4 = Point(midx + 1, midy + 1)
        tr4 = topRight

        # Recurse into all quadrants (each one prunes itself using hasShips)
        return (
            self.countShips(sea, tr1, bl1) +
            self.countShips(sea, tr2, bl2) +
            self.countShips(sea, tr3, bl3) +
            self.countShips(sea, tr4, bl4)
        )
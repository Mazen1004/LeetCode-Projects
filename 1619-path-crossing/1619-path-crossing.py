class Solution:
    def isPathCrossing(self, path: str) -> bool:
        coordsSet = set() #set containing coords

        coords = (0,0)
        coordsSet.add(coords)

        for direction in path:
            if direction == 'N':
                coords = (coords[0], coords[1] + 1)
            elif direction == 'S':
                coords = (coords[0], coords[1] - 1)
            elif direction == 'E':
                coords = (coords[0] + 1, coords[1])
            elif direction == 'W':
                coords = (coords[0] - 1, coords[1])

            if coords in coordsSet:
                return True
            coordsSet.add(coords)

        return False        
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        units = 0
        currentSize = 0

        # sort by maximum number of units per box
        boxTypes.sort(key=lambda x: x[1], reverse= True)
        print(boxTypes)

        for numberofboxes, numberofunitsperbox in boxTypes:
            count = 0
            while count < numberofboxes and currentSize < truckSize:
                count += 1
                units = units + numberofunitsperbox
                currentSize += 1

        return units
        
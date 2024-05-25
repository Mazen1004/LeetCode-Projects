class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        #whatever appears as cityB once is destination
        dictmap = {}
        for path in paths:
            dictmap[path[0]] = path[1]

        dest_city = paths[0][1] #start with any destination city

        while dest_city in dictmap:
            dest_city = dictmap[dest_city]
            print(dest_city)


        print("done loop")
        print(dest_city)
        return dest_city

    
class Solution:
    def maximum69Number (self, num: int) -> int:
        
        #convert num to str list (remember strings are immutable)
        stringnum = list(str(num))
        count = 0
        print(stringnum)

        for i in range(len(stringnum)):
            if stringnum[i] == "6" and count == 0:
                count += 1
                stringnum[i] = "9"
                break


        #convert back to int before returning
        return int("".join(stringnum))        
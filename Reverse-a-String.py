def reverseString(s):
        List = []
        for i in range (len(s)-1, -1):
            print(s[i])
            List = List + [s[i]]
            print(List) 
        return List 
#assert(reverseString(["h", "e", "l", "l", "o"]) == ["o", "l", "l", "e", "h"])
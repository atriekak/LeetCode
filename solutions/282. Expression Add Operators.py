            #preceding 0
            if idx != i and num[idx] == '0':    # 0 is fine; 05 is not
                continue
            
            curr = int(num[idx : i + 1])
            
            length = len(strBuilder)
            if idx == 0:
                strBuilder.append(str(curr))    #action
                self.helper(num, target, strBuilder, i+1, calc + curr, curr)    #recursion
                del strBuilder[length:]    #backtracking
            else:
                strBuilder.append('+')
                strBuilder.append(str(curr))
                self.helper(num, target, strBuilder, i+1, calc + curr, curr)
                del strBuilder[length:]
                
                strBuilder.append('-')
                strBuilder.append(str(curr))
                self.helper(num, target, strBuilder, i+1, calc - curr, -curr)
                del strBuilder[length:]
                
                strBuilder.append('*')
                strBuilder.append(str(curr))
                self.helper(num, target, strBuilder, i+1, calc - tail + tail*curr, tail*curr)
                del strBuilder[length:]
                
    #Solution 2
    """
    def addOperators(self, num: str, target: int) -> List[str]:
        #Approach: Recursion; str is an immutable data structure
        #Time Complexity: O(n * 4^n)
        #Space Complexity: O(4^n) // 4 deep copies at every point
        #where, n is the length of nums
        
        self.result = []
        self.helper(num, target, "", 0, 0, 0)
        return self.result
    
    def helper(self, num, target, path, idx, calc, tail):
        #base
        if idx == len(num):
            if calc == target:
                self.result.append(path)
            return
        
        #logic
        for i in range(idx, len(num)):
            #preceding 0
            if idx != i and num[idx] == '0':    # 0 is fine; 05 is not
                continue
            
            curr = int(num[idx : i + 1])
            
            if idx == 0:
                self.helper(num, target, path + str(curr), i + 1, curr, curr)
            else:
                self.helper(num, target, path + "+" + str(curr), i+1, calc + curr, curr)
                self.helper(num, target, path + "-" + str(curr), i+1, calc - curr, -curr)
                self.helper(num, target, path + "*" + str(curr), i+1, calc - tail + tail*curr,                             tail*curr)
    """

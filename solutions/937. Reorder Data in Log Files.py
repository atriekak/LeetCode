class Solution:
    #Solution 1
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        #Approach: Custom sorting only letter logs
        #Time Complexity: O(m log m)
        #Space Complexity: O(n)
        #where, m and n are the number of letter and digit logs, respectively
        
        letter_logs = []
        digit_logs = []
        for log in logs:
            if log[-1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
                
        letter_logs.sort(key = lambda x: tuple(reversed(x.split(' ', 1))))
        
        letter_logs.extend(digit_logs)
        return letter_logs
    
    #Solution 2
    """
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        #Approach: Custom sorting the entire logs array
        #Time Complexity: O((m+n) log (m+n))
        #Space Complexity: O(1)
        #where, m and n are the number of letter and digit logs, respectively
        
        logs.sort(key = self.custom_sort_order)
        return logs
        
    def custom_sort_order(self, log):
        id, content = log.split(' ', 1)
        
        if content[0].isalpha():
            return (0, content, id)
        else:
            return (1, None, None)
    """

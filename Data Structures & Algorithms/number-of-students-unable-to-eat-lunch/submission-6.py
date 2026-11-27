from collections import Counter

class Solution:
    def countStudents(self, students, sandwiches):
        count = Counter(students)

        for i in sandwiches:
            if count[i] == 0:
                return sum(count.values())
            count[i] -= 1
        
        return 0
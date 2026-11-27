from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        queue_student = deque(students)
        queue_sandwich = deque(sandwiches)

        passes = 0 
        
        while queue_student:

            if queue_student[0] == queue_sandwich[0]:
                queue_student.popleft()
                queue_sandwich.popleft()
                passes = 0
            else:
                queue_student.append(queue_student.popleft())
                passes += 1
            
            if passes == len(queue_student):
                return len(queue_student)
        
        return 0




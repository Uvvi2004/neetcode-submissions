from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        queue_student = deque(students)
        queue_sandwich = deque(sandwiches)

        counter = len(sandwiches) * 10
        
        while counter:

            if not queue_student:
                return 0

            if queue_student[0] == queue_sandwich[0]:
                queue_student.popleft()
                queue_sandwich.popleft()
            else:
                queue_student.append(queue_student.popleft())

            counter -= 1
        
        return len(queue_student)




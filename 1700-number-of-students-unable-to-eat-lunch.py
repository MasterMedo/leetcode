class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        preference = [0, 0]
        for student in students:
            preference[student] += 1

        for sandwich in sandwiches:
            if preference[sandwich] > 0:
                preference[sandwich] -= 1
            else:
                break

        return sum(preference)

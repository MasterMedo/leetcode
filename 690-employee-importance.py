class Solution:
    def getImportance(self, employees: list['Employee'], id: int) -> int:
        def calcImportance(e: 'Employee') -> int:
            return sum(calcImportance(employees[i]) for i in e.subordinates) + e.importance

        employees = {employee.id: employee for employee in employees}
        return calcImportance(employees[id])

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for operator in operations:
            if operator == 'D':
                record.append(2 * record[-1])
            elif operator == 'C':
                record.pop()
            elif operator == '+': record.append(record[-1] + record[-2])
            else: record.append(int(operator))
        return sum(record)
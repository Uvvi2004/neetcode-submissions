class Solution:
    def calPoints(self, operations: List[str]) -> int:


        record = []
        
        for operation in operations:

            if operation == "+":
                second = record.pop()
                first = record.pop()
                add = first + second

                record.append(first)
                record.append(second)
                record.append(add)
            
            elif operation == "C":
                record.pop()
            
            elif operation == "D":

                value = record.pop()

                doubled = value * 2

                record.append(value)
                record.append(doubled)
            else:
                record.append(int(operation))
            

        return sum(record)

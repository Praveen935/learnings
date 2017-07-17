class Operation(object):
    operator_list = ('+', '-', '*', '/')

    def __init__(self):
        self.operand_one = None
        self.operand_two = None
        self.operator = None
        self.result = None

    def set_operand_one(self, operand_one):
        self.operand_one = operand_one

    def set_operator_two(self, operand_two):
        self.operand_two = operand_two

    def set_operator(self, operator):
        self.operator = operator

    def perform_operation(self):
        if self.operand_one is None:
            self.get_prompt()
        elif self.operand_two is None:
            self.get_prompt()
        else:
            self.calculate()

    def calculate(self):
        try:
            self.result = {
                '+': Calculator.perform_add(self.operand_one, self.operand_two),
                '-': Calculator.perform_subtract(self.operand_one, self.operand_two),
                '*': Calculator.perform_multiplication(self.operand_one, self.operand_two),
                '/': Calculator.perform_division(self.operand_one, self.operand_two),
            }[self.operator]
        except Exception, error:
            self.result = str(error)
        finally:
            print self.result

    def get_prompt(self):
        if self.operator == '+' or self.operator == '-' or self.operator == '*':
            if self.operand_one is None:
                entered_value = raw_input("Enter operand 1\n")
                if entered_value.isdigit():
                    self.operand_one = int(entered_value)
                else:
                    print "Invalid input. only numbers are allowed\n"
            else:
                entered_value = raw_input("Enter operand 2\n")
                if entered_value.isdigit():
                    self.operand_two = int(entered_value)
                else:
                    print "Invalid input. only numbers are allowed\n"
        elif self.operator == '/':
            if self.operand_one is None:
                entered_value = raw_input("Enter numerator\n")
                if entered_value.isdigit():
                    self.operand_one = int(entered_value)
                else:
                    print "Invalid input. only numbers are allowed\n"
            else:
                entered_value = raw_input("Enter denominator\n")
                if entered_value.isdigit():
                    self.operand_two = int(entered_value)
                else:
                    print "Invalid input. only numbers are allowed\n"

        self.perform_operation()


class Calculator(object):
    @staticmethod
    def perform_add(operand_one, operand_two):
        return operand_one + operand_two

    @staticmethod
    def perform_subtract(operand_one, operand_two):
        return operand_one - operand_two

    @staticmethod
    def perform_multiplication(operand_one, operand_two):
        return operand_one * operand_two

    @staticmethod
    def perform_division(numerator, denominator):
        return numerator / denominator


def main():
    while True:
        operator = raw_input(
            """Select operation: \n + for Addition \n - for Subtraction\n * for multiplication \n / for division >\n""")

        if Operation.operator_list.__contains__(operator):
            operation = Operation()
            operation.set_operator(operator)
            operation.get_prompt()
        else:
            print "Operation not supported"
            
if __name__ == '__main__':
    main()

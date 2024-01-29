print("HEYYYY IM your personal calculator, please give me a simple two value with a single expression such as\
 input like 'a + b'")


class Calculator:
    def __init__(self, first_element: str, operation: str, second_element: str):
        self.first_element: str = first_element
        self.operation: str = operation
        self.second_element: str = second_element

    def _validate_numbers(self) -> bool:
        return self.first_element.isnumeric() and self.second_element.isnumeric()

    def _validate_operator(self) -> bool:
        return self.operation == '*' or self.operation == '+' or self.operation == '-' or self.operation == '/'

    def validate(self) -> bool:
        return self._validate_operator() and self._validate_numbers()

    def __str__(self):
        return f"{self.first_element} {self.operation} {self.second_element} = "

    def get_answer(self) -> int:
        return eval(str(self.first_element + self.operation + self.second_element))


while True:
    text_input = input("Input expression: ")
    text_input = ''.join(text_input.split(' '))

    i = 0
    operator = '-'
    while i < len(text_input):
        if text_input[i].isnumeric():
            i += 1
            continue
        else:
            if text_input[i] == '+' or text_input[i] == '-' or text_input[i] == '/' or text_input[i] == '*':
                operator = text_input[i]
            else:
                print("The elements must be integers, and the operator must be one of the operators '+-*/'")
                break
        i += 1
    else:
        text = text_input.split(operator)

        if ''.join(text).lower() == "done":
            print("Ending the session. Bye!")
            break

        if len(text) != 2:
            print("The expression should have 2 numbers and 1 operator only")
        else:
            expression = Calculator(text[0], operator, text[1])
            if expression.validate():
                if int(expression.second_element) == 0:
                    print("Division by 0 is undefined")
                    continue
                print(expression, end='')
                print(expression.get_answer())
            else:
                print("Invalid expression. There should be 2 numbers and one operator of a type '+-*/'")
                continue

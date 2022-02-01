import re
# from self import self
from stack_project import Stack


class Exp:
    def __init__(self, infix: str):
        self.precedence = {"(": 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        self.infix = infix

    def create_space(self):
        list1 = ["+", "-", "*", "/", "^", "(", ")"]
        result = ""
        for i in self.minus():
            if i in list1:
                result += " " + i + " "
            else:
                result += i
        return result.split()

    def infixToPostfix(self):
        s = Stack(100)
        result = []
        for i in self.create_space():
            if bool(re.match("^\\d+$", i)):
                result.append(int(i))
            elif bool(re.match("^\\d+\\.\\d+$", i)):
                result.append(float(i))
            elif i == "(":
                s.push(i)
            elif i == ")":
                while not s.isEmpty() and not s.peek() == "(":
                    result.append(s.pop())
                s.pop()
            else:
                if i in ["+", "-", "*", "/"]:
                    while (not s.isEmpty()) and self.precedence[i] <= self.precedence[s.peek()]:
                        result.append(s.pop())
                    s.push(i)
                elif i in ["^"]:
                    while (not s.isEmpty()) and self.precedence[i] < self.precedence[s.peek()]:
                        result.append(s.pop())
                    s.push(i)

        while not s.isEmpty():
            result.append(s.pop())
        # print(s.peek())
        return result

    def EvaluatePostfix(self):
        s = Stack(100)
        # string = ""
        my_list = []
        for i in self.infixToPostfix():
            if isinstance(i, int) or isinstance(i, float):
                s.push(i)
            else:
                first = s.pop()
                second = s.pop()

                if i == "+":
                    s.push(first + second)
                elif i == "-":
                    s.push(second - first)
                elif i == "*":
                    s.push(second * first)
                elif i == "/":
                    s.push(second / first)
                elif i == "^":
                    s.push(second ** first)
                else:
                    raise Exception("Error")
                # print(second, i, first, "=", s.peek())

                # string = f'{second} {i} {first} = {s.peek()}'
                my_list.append(f'{second} {i} {first} = {s.peek()}')
                '''
                **return these str**

                second_text = str(second)
                i_text = str(i)
                first_text = str(first)
                equal_text = "="
                s.peek_text = str(s.peek())
                '''
        return [s.pop(), my_list]
        # return [s.pop(), string]

    def minus(self):
        result = ""
        for i in self.infix:
            if (i == "-" or i == "+") and (self.infix.index(i) == 0 or self.infix[self.infix.index(i) - 1] == "("):
                result += "0"
            result += i
        return result



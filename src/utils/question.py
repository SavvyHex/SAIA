import random

class Question:
    def __init__(self) -> None:
        self.op = random.choice(["+", "-", "*", "/"])
        self.a = random.randint(1, 20)
        self.b = random.randint(1, 20)
        self.get_ans()
        self.get_options()

    def make_fair(self, ini_ans:float) -> str:
        ans = str(ini_ans)
        return ans if len(ans)<5 else ans[:5]

    def get_ans(self) -> None:
        op = self.op
        if op == "+":
            self.ans = self.a + self.b
        elif op == "-":
            self.ans = self.a - self.b
        elif op == "*":
            self.ans = self.a * self.b
        elif op == "/":
            self.ans = self.a / self.b

    def get_options(self) -> None:
        self.options = list()
        indices = [0, 1, 2, 3]
        options = [0, 0, 0, 0]
        o1 = self.ans
        o2 = self.ans + random.randint(1, 5) if random.randint(1, 2)%2 == 0 else self.ans - random.randint(1, 5)
        o3 = self.ans + random.randint(1, 5) if random.randint(1, 2)%2 == 0 else self.ans - random.randint(1, 5)
        o4 = self.ans + random.randint(1, 5) if random.randint(1, 2)%2 == 0 else self.ans - random.randint(1, 5)
        ops = [o1, o2, o3, o4]
        while indices:
            index = random.choice(indices)
            choice = random.choice(ops)
            options[index] = choice
            indices.remove(index)
            ops.remove(choice)
        self.ans_opt = chr(options.index(self.ans) + 97)

        for option in options:
            self.options.append(self.make_fair(option))

    def __str__(self) -> str:
        return f"""What is {self.a}{self.op}{self.b}?
a) {self.options[0]}
b) {self.options[1]}
c) {self.options[2]}
d) {self.options[3]}"""

    def __repr__(self) -> str:
        return str(self)
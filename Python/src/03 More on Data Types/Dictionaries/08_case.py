def convert(n):
    case = {
        0: "zero",
        1: "one",
        2: "two",
    }
    return case.get(n, "nothing")


print convert(1)
print convert(2)
print convert(5)


def arithmetic(expr):
    lhs, op, rhs = expr.split()
    lhs, rhs = int(lhs), int(rhs)
    case = {
        '+': lambda: lhs + rhs,
        '-': lambda: lhs - rhs,
        '*': lambda: lhs * rhs,
        '/': lambda: lhs / rhs,
    }
    return case[op]()

print arithmetic('15 + 3')
print arithmetic('15 - 3')
print arithmetic('15 * 3')
print arithmetic('15 / 3')

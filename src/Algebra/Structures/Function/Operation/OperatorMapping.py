from src.Algebra.Structures.Function.Operation.ComputationalGraphPart import Add, Div, Mul, Pow, Sub

operator_mapping = {
    "+": Add,
    "*": Mul,
    "/": Div,
    "^": Pow,
    "-": Sub
}

operators = ("^", "*", "/", "+", "-")

operator_priority = [
    "^", "*", "/", "+", "-"
]

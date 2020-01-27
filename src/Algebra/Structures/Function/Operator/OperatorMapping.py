from src.Algebra.Structures.Function.Operator.Add import Add
from src.Algebra.Structures.Function.Operator.Div import Div
from src.Algebra.Structures.Function.Operator.Mul import Mul
from src.Algebra.Structures.Function.Operator.Pow import Pow
from src.Algebra.Structures.Function.Operator.Sub import Sub

operator_mapping = {
    "+": Add,
    "*": Mul,
    "/": Div,
    "^": Pow,
    "-": Sub
}

operator_priority = [
    "^", "*", "/", "+", "-"
]
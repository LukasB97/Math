from src.Algebra.Structures.Function.Operation.Add import Add
from src.Algebra.Structures.Function.Operation.Div import Div
from src.Algebra.Structures.Function.Operation.Mul import Mul
from src.Algebra.Structures.Function.Operation.Pow import Pow
from src.Algebra.Structures.Function.Operation.Sub import Sub

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
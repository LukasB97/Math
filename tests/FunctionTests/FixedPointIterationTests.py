import parser
import unittest
from time import time

from src.AlgebraicStructures.Function.FunctionParser import FunctionParser
from src.AlgebraicStructures.Function.Operator1 import Operator
from src.Calculus.FixedPointIteration import NewtonsMethod


class FixedPointIterationTests(unittest.TestCase):

    def test_linear_function(self, x=2.1, a=4, y=3.4):
        graph = FunctionParser.parse_string("10+x^2")
        r1 = NewtonsMethod.start(graph, 1, 30)
        print("x=", r1, " f(x)=", graph.evaluate(x=r1))
        graph = FunctionParser.parse_string("1+0.009*x^3")
        r2 = NewtonsMethod.start(graph, 0, 30)
        print("x=", r2, " f(x)=", graph.evaluate(x=r2))



    def test_get_bracket_section(self):
        input_data = list("a((c+3*5)*3)")
        result = list("c+3*5")
        self.assertEqual(FunctionParser.get_bracket_section(input_data, 2), result)

    def test_build_definition_list(self):
        input_data = "a((c+3*5)*3)"
        result = list(input_data)
        result[4] = Operator.ADD
        result[6] = Operator.MUL
        result[9] = Operator.MUL
        self.assertEqual(FunctionParser.build_definition_list(input_data), result)





    def test_preprocessing(self):
        a = "x y* a+ (5*2)c"
        self.assertEqual(
            FunctionParser.preprocess_string(a),
            "x*y*a+(5*2)*c"
        )

    def test_parse(self, x=2.1, a=4, y=3.4):
        graph = FunctionParser.parse_string("x y* a+ (5*2)")
        result = graph.evaluate(x=x, y=y, a=a)
        self.assertEqual(result, x*y*a+(5*2))
        graph = FunctionParser.parse_string("x^2+5")
        result = graph.evaluate(x=x)
        self.assertEqual(result, x**2+5)
        graph = FunctionParser.parse_string("x^x*3")
        result = graph.evaluate(x=x)
        self.assertEqual(result, x**x*3)
        graph = FunctionParser.parse_string("a^(14*x)+13*2-1")
        result = graph.evaluate(x=x, a=a)
        self.assertEqual(result, a**(14*x)+13*2-1)
        graph = FunctionParser.parse_string("(x+2)13*x^2")
        result = graph.evaluate(x=x)
        self.assertEqual(result, (x+2)*13*x**2)
        graph = FunctionParser.parse_string("(x^3*4+(4/y*(13+2)))*5")
        result = graph.evaluate(x=x, y=y)
        self.assertEqual(result, (x**3*4+(4/y*(13+2)))*5)

    def test_performance(self):
        #13.12.19: std 5x faster
        eq = "(x+2)*13*x**2"
        time1 = time()
        for i in range(100):
            code = parser.expr(eq).compile()
            x = 10
            eval(code)
        time2 = time()
        print(time2-time1)
        eq = "(x+2)13*x^2"
        time1 = time()
        for i in range(100):
            graph = FunctionParser.parse_string(eq)
            result = graph.evaluate(x=10)
        time2 = time()
        print(time2-time1)

    def test_profile(self):
        eq = "(x+2)13*x^2"
        for i in range(100):
            graph = FunctionParser.parse_string(eq)
            result = graph.evaluate(x=10)

if __name__ == '__main__':
    unittest.main()


from src.Algebra.Structures.Function.Variable import Variable
from src.Algebra.Structures.Function.Function import Function
from src.Algebra.Structures.Function.Operator1 import Operator


class FunctionParser:

    @classmethod
    def parse_brackets(cls, definition_input: list) -> list:
        definition = list()
        last_end = 0
        while "(" in definition_input[last_end:]:
            start = definition_input.index("(", last_end)
            bracket_section = cls.get_bracket_section(definition_input, start)
            definition += definition_input[last_end:start]
            last_end = start + len(bracket_section) + 1
            definition.append(cls.parse_list(bracket_section))
        definition += definition_input[last_end + 1:]
        assert "(" not in definition and ")" not in definition
        return definition

    @classmethod
    def parse_string(cls, definition_string: str):
        definition_string = cls.preprocess_string(definition_string)
        definition = cls.build_definition_list(definition_string)
        if "(" in definition_string:
            definition = cls.parse_brackets(definition)
        definition = cls.build_graph(definition)
        return definition[0]

    @classmethod
    def parse_list(cls, definition):
        if "(" in definition:
            definition = cls.parse_brackets(definition)
        definition = cls.build_graph(definition)
        return definition[0]

    @classmethod
    def build_definition_list(cls, definition_string: str):
        definition = list()
        is_number = False
        number = ""
        for i in range(len(definition_string)):
            if definition_string[i].isnumeric() or (definition_string[i] in [",", "."] and is_number):
                number += definition_string[i]
                is_number = True
            elif is_number:
                is_number = False
                definition.append(float(number))
                number = ""
            if definition_string[i] in ["*", "/", "+", "-", "^"]:
                definition.append(Operator.get(definition_string[i]))
            elif definition_string[i].isalpha():
                definition.append(Variable(definition_string[i]))
            elif definition_string[i] in ["(", ")"]:
                definition.append(definition_string[i])
        if is_number:
            definition.append(float(number))
        return definition

    @classmethod
    def preprocess_string(cls, definition_string: str) -> str:
        definition_string = definition_string.replace(" ", "")
        definition_string = cls.preprocess_multiply(definition_string)
        return definition_string

    @classmethod
    def preprocess_multiply(cls, definition_string: str) -> str:
        for i in range(len(definition_string) - 1):
            if definition_string[i].isalpha():
                if definition_string[i + 1].isalnum() or definition_string[i + 1] == "(":
                    definition_string = cls.preprocess_multiply(
                        definition_string[:i + 1] + "*" + definition_string[i + 1:])
                    break
            if definition_string[i] == ")":
                if definition_string[i + 1].isalnum() or definition_string[i + 1] == "(":
                    definition_string = cls.preprocess_multiply(
                        definition_string[:i + 1] + "*" + definition_string[i + 1:])
                    break
        return definition_string

    @classmethod
    def build_graph(cls, definition: list):
        definition = cls.build_for_operator(definition, Operator.POW)
        definition = cls.build_for_operator(definition, Operator.DIV)
        definition = cls.build_for_operator(definition, Operator.MUL)
        definition = cls.build_for_operator(definition, Operator.SUB)
        definition = cls.build_for_operator(definition, Operator.ADD)
        return definition

    @classmethod
    def build_part(cls, op_1, operator, op2):
        return Function(operator, [op_1, op2])

    @classmethod
    def build_for_operator(cls, definition: list, op: Operator):
        new_definition = list()
        last_end = -1
        while op in definition:
            start = definition.index(op) - 1
            new_definition += definition[last_end + 1:start]
            last_end = start + 1
            part = cls.build_part(definition[start], op, definition[start + 2])
            new_definition.append(part)
            definition.pop(start)
            definition.pop(start)
            definition.pop(start)
            definition.insert(start, part)
        new_definition += definition[last_end + 1:]
        # return new_definition
        return definition

    @classmethod
    def get_bracket_section(cls, definition: list, start_index):
        assert definition[start_index] == "("
        opening_count = 1
        closing_count = 0
        for i in range(start_index + 1, len(definition)):
            if definition[i] == "(":
                opening_count += 1
            elif definition[i] == ")":
                closing_count += 1
            if opening_count == closing_count:
                return definition[start_index + 1: i]
        raise ValueError("Invalid Format: " + str(definition))
